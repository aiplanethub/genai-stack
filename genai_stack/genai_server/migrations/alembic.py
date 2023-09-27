from pathlib import Path
from typing import Any, Callable, List, Sequence, Union
from sqlalchemy.engine import Engine
from sqlalchemy.sql.schema import MetaData
from alembic.config import Config
from alembic.script import ScriptDirectory
from alembic.environment import EnvironmentContext
from alembic.migration import MigrationContext

_RevIdType = Union[str, Sequence[str]]

class Alembic:
    """Alembic environment and migration API."""

    def __init__(self, database_uri:str, engine:Engine, meta_data:MetaData, table_name:str):

        self.engine = engine
        self.meta_data = meta_data
        self.table_name = table_name

        # Config object represents the configuration passed to the Alembic environment
        # it is needed for the following use cases:
        # to create a ScriptDirectory, which allows you to work with the actual script files in a migration environment
        # to create an EnvironmentContext, which allows you to actually run the env.py module within the migration environment
        # to programmatically run any of the commands in the Commands module.
        self.config = Config()

        # Setting the migrations folder which is present in genai_server.
        self.config.set_main_option(
            "script_location",str(Path(__file__).parent)
        )

        # Setting the versions folder which is present in genai_server/migrations folder.
        self.config.set_main_option(
            "version_locations", str(Path(__file__).parent / "versions")
        )

        # Setting the database uri
        self.config.set_main_option(
            "sqlalchemy.url", database_uri
        )

        # object provides programmatic access to the Alembic version files present in genai_server/migrations/versions folder
        self.script_directory = ScriptDirectory.from_config(self.config)

        # Environment context object is required to configure connection to database, metadata of schemas and 
        # the custom migration function to run migration.
        self.environment_context = EnvironmentContext(
            self.config, self.script_directory
        )


    @property    
    def current_head(self) -> str:
        """
        This method returns the current head revision.

        Return:
            a string revision number.
        """
        return self.script_directory.get_current_head()
    
    @property
    def current_base(self) -> str:
        """
        This method returns the current down revision.

        Return:
            a string revision number.
        """
        return self.script_directory.get_base()
    
    def run_migrations(
        self,
        fn: Callable[[_RevIdType, MigrationContext], List[Any]],
    ) -> None:
        """Run an online migration function in the current migration context.

        Args:
            fn: Migration function to run. If not set, the function configured
                externally by the Alembic CLI command is used.
        """

        with self.engine.connect() as connection:
            self.environment_context.configure(
                connection=connection,
                target_metadata=self.meta_data,
                fn=fn
            )

            with self.environment_context.begin_transaction():
                self.environment_context.run_migrations()          
    
    def db_is_empty(self) -> bool:
        """Check if the database is empty.

        Returns:
            True if the database is empty, False otherwise.
        """
        # Check the existence of any of the database tables
        return not self.engine.dialect.has_table(
            self.engine.connect(), table_name=self.table_name
        )
    
    def upgrade(self, revision:str = "heads") -> None:
        """
        This method upgrades the db with current head revision.
        """
        def do_upgrade(rev: _RevIdType, context: Any) -> List[Any]:
            return self.script_directory._upgrade_revs(
                revision, rev 
            )

        self.run_migrations(do_upgrade)


    def downgrade(self, revision:str) -> None:
        """
        This method downgrades the db with the provided down revision.
        """
        def do_downgrade(rev: _RevIdType, context: Any) -> List[Any]:
            return self.script_directory._downgrade_revs(
                revision, rev
            )

        self.run_migrations(do_downgrade)