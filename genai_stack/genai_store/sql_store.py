from pydantic import BaseModel
from typing import Optional
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData

from genai_stack.genai_server.migrations.alembic import Alembic


class SQLStoreConfiguration(BaseModel):
    """
    Data Model for SQL Store Configurations.

    Args:
        url : The database path.
        meta_data : The meta_data object of schemas
        table_name : any table name from schemas, to check whether the database contains the tables or not.
    """
    class Config:
        arbitrary_types_allowed = True

    url:str
    meta_data:MetaData
    table_name:str


class SQLStore:
    """Store Implementation that uses SQL database backend."""

    config:SQLStoreConfiguration
    config_class: SQLStoreConfiguration = SQLStoreConfiguration
    _engine: Optional[Engine] = None
    _alembic:Optional[Alembic] = None

    def __init__(self, url:str, meta_data:MetaData, table_name:str) -> None :

        self.config = self.config_class(url=url, meta_data=meta_data, table_name=table_name)
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

        self._engine = create_engine(url=self.config.url)

        self._alembic = Alembic(
            database_uri=self.config.url,
            engine=self.engine,
            meta_data=self.config.meta_data,
            table_name=self.config.table_name
        )
        
        self.migrate_database()

    def migrate_database(self):
        self.alembic.upgrade()