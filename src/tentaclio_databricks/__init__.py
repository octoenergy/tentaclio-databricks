"""tentaclio is a library that tries to unify how to load, store data.
The main use cases in mind are ETL processes and notebooks, but can be used in many other contexts.
The main benefits are:
    * url based resource management.
    * same function to open readers and writers for resources of different natures.
    Just change the url, the code remains the same.
    * The same for dbs, create clients with ease and use them regardless
    the underlying implementation (thanks to sqlalchemy).
    * Credentials management that allows a distributed credentials storage.
"""
from tentaclio import *  # noqa

from .clients.databricks_client import DatabricksClient


# Add DB registry
DB_REGISTRY.register("databricks+pyodbc", DatabricksClient)  # type: ignore
