"""This package implements the tentaclio databricks+pyodbc database client """
from tentaclio import *  # noqa

from .clients.databricks_client import DatabricksClient


# Add DB registry
DB_REGISTRY.register("databricks+pyodbc", DatabricksClient)  # type: ignore
