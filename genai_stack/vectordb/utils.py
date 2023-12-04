from langchain.schema import Document
from pydantic import BaseModel


def use_pysqlite3():
    """
    Swap std-lib sqlite3 with pysqlite3.
    """
    import platform
    import sqlite3

    if platform.system() == "Linux" and sqlite3.sqlite_version_info < (3, 35, 0):
        try:
            # According to the Chroma team, this patch only works on Linux
            import datetime
            import subprocess
            import sys

            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "pysqlite3-binary",
                    "--quiet",
                    "--disable-pip-version-check",
                ]
            )

            __import__("pysqlite3")
            sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

            # Let the user know what happened.
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
            print(
                f"{current_time}",
                "Swapped std-lib sqlite3 with pysqlite3 for ChromaDb compatibility.",
                f"Your original version was {sqlite3.sqlite_version}.",
            )
        except Exception as e:
            # Escape all exceptions
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
            print(
                f"{current_time}",
                "Failed to swap std-lib sqlite3 with pysqlite3 for ChromaDb compatibility.",
                "Error:",
                e,
            )


class HybridSearchResponse(BaseModel):
    query: str
    metadata: dict
    score: float
    isSimilar: bool
    document: Document
