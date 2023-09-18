from pydantic import BaseModel
from typing import Optional
from enum import Enum
from sqlalchemy.engine import Engine


class StoreType(Enum):
    """Store Backend Types."""

    SQL = "sql"


class SQLDatabaseDriver(Enum):
    """SQL database drivers supported by the SQL Store."""

    MYSQL = "mysql"
    SQLITE = "sqlite"


class SQLStoreConfiguration(BaseModel):
    """Data Model for SQL Store Configurations."""

    type: StoreType = StoreType.SQL
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


class SQLStore:
    """Store Implementation that uses SQL database backend."""

    config: SQLStoreConfiguration
    _engine: Optional[Engine] = None
    _alembic = None

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

    def _initialise(self):
        pass

    def _create_mysql_database(self):
        pass

    def migrate_database(self):
        pass