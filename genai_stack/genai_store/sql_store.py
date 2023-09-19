from pydantic import BaseModel
from typing import Optional, Dict, Any, Tuple, cast
from sqlalchemy.engine import Engine, make_url
from sqlalchemy.exc import (
    OperationalError,
)
from sqlalchemy import URL, create_engine, text
import pymysql
import os

from genai_stack.enum_utils import StrEnum


def _is_mysql_missing_database_error(error: OperationalError) -> bool:
    """Checks if the given error is due to a missing database.

    Args:
        error: The error to check.

    Returns:
        If the error if because the MySQL database doesn't exist.
    """
    from pymysql.constants.ER import BAD_DB_ERROR

    if not isinstance(error.orig, pymysql.err.OperationalError):
        return False

    error_code = cast(int, error.orig.args[0])
    return error_code == BAD_DB_ERROR


class StoreType(StrEnum):
    """Store Backend Types."""

    SQL = "sql"


class SQLDatabaseDriver(StrEnum):
    """SQL database drivers supported by the SQL Store."""

    MYSQL = "mysql"
    SQLITE = "sqlite"


class SQLStoreConfiguration(BaseModel):
    """Data Model for SQL Store Configurations."""

    type: StoreType = StoreType.SQL
    url:str
    driver:Optional[SQLDatabaseDriver] = None
    database:Optional[str] = None
    username:Optional[str] = None
    password:Optional[str] = None
    ssl_ca:Optional[str] = None
    ssl_cert:Optional[str] = None
    ssl_key:Optional[str] = None
    ssl_verify_server_cert:bool = False
    pool_size:int = 20
    max_overflow:int = 20
    pool_pre_ping:bool = True 

    def get_sql_config(self) ->  Tuple[str, Dict[str, Any], Dict[str, Any]]:
        """
        Get the SQL engine configuration for the SQL Store.

        Returns:
            The URL and connection arguments for the SQL engine.

        Raises:
            NotImplementedError: If the SQL driver is not supported.
        """
        sql_url = make_url(self.url)
        sqlalchemy_connect_args: Dict[str, Any] = {}
        engine_args = {}
        
        if sql_url.drivername == SQLDatabaseDriver.SQLITE:
            assert self.database is not None
            # The following default value is needed for sqlite to avoid the
            # Error:
            #   sqlite3.ProgrammingError: SQLite objects created in a thread can
            #   only be used in that same thread.
            # sqlalchemy_connect_args = {"check_same_thread": False}
        elif sql_url.drivername == SQLDatabaseDriver.MYSQL:
            assert self.database is not None
            assert self.username is not None
            assert self.password is not None
            assert sql_url.host is not None
            
            engine_args = {
                "pool_size": self.pool_size,
                "max_overflow": self.max_overflow,
                "pool_pre_ping": self.pool_pre_ping,
            }

            sql_url = sql_url._replace(
                drivername="mysql+pymysql",
                username=self.username,
                password=self.password,
                database=self.database,
            )

            sqlalchemy_ssl_args: Dict[str, Any] = {}

            # Handle SSL params
            for key in ["ssl_key", "ssl_ca", "ssl_cert"]:
                ssl_setting = getattr(self, key)
                if not ssl_setting:
                    continue
                if not os.path.isfile(ssl_setting):
                    raise ValueError(
                        f"Database SSL setting `{key}` is not a file. "
                    )
                sqlalchemy_ssl_args[key.lstrip("ssl_")] = ssl_setting
            if len(sqlalchemy_ssl_args) > 0:
                sqlalchemy_ssl_args[
                    "check_hostname"
                ] = self.ssl_verify_server_cert
                sqlalchemy_connect_args["ssl"] = sqlalchemy_ssl_args
        else:
            raise NotImplementedError(
                f"SQL driver `{sql_url.drivername}` is not supported."
            )

        return str(sql_url), sqlalchemy_connect_args, engine_args

class SQLStore:
    """Store Implementation that uses SQL database backend."""

    config_class: SQLStoreConfiguration = SQLStoreConfiguration
    _engine: Optional[Engine] = None
    _alembic = None

    def __init__(self, *args, **kwargs) -> None :
        self.config = self.config_class(**kwargs)
        self._initialise()

    @property
    def engine(self) -> Engine:
        """The SQLAlchemy engine.

        Returns:
            The SQLAlchemy engine.

        Raises:
            ValueError: If the store is not initialized.
        """
        if not self._engine:
            raise ValueError("Store not initialized")
        return self._engine
    
    @property
    def alembic(self) -> None:
        """The Alembic wrapper.

        Returns:
            The Alembic wrapper.

        Raises:
            ValueError: If the store is not initialized.
        """
        if not self._alembic:
            raise ValueError("Store not initialized")
        return self._alembic

    def _initialise(self) -> None:
        url, connect_args, engine_args = self.config.get_sql_config()

        self._engine = create_engine(
           url=url, connect_args=connect_args, **engine_args
        )

        # SQLite: As long as the parent directory exists, SQLAlchemy will
        # automatically create the database.
        if (
            self.config.driver == SQLDatabaseDriver.SQLITE
            and self.config.database
            and not os.path.exists(os.path.dirname(url.replace("sqlite:///","")))
        ):  
           os.makedirs(os.path.dirname(url.replace("sqlite:///","")))

        if (
            self.config.driver == SQLDatabaseDriver.MYSQL
            and self.config.database
        ):
            try:
                self._engine.connect()
            except OperationalError as e:
                print(
                    "Failed to connect to mysql database `%s`.",
                    self._engine.url.database,
                )

                if _is_mysql_missing_database_error(e):
                    self._create_mysql_database(
                        url=self._engine.url,
                        connect_args=connect_args,
                        engine_args=engine_args,
                    )
                else:
                    raise
                

    def _create_mysql_database(
        self,
        url: URL,
        connect_args: Dict[str, Any],
        engine_args: Dict[str, Any],
    ) -> None:
        """Creates a mysql database.

        Args:
            url: The URL of the database to create.
            connect_args: Connect arguments for the SQLAlchemy engine.
            engine_args: Additional initialization arguments for the SQLAlchemy
                engine
        """
        print("Trying to create database %s.", url.database)
        master_url = url._replace(database=None)
        master_engine = create_engine(
            url=master_url, connect_args=connect_args, **engine_args
        )
        query = f"CREATE DATABASE IF NOT EXISTS {self.config.database}"
        try:
            connection = master_engine.connect()
            connection.execute(text(query))
        finally:
            connection.close()

    def migrate_database(self):
        pass