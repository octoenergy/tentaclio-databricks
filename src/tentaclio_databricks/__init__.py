"""This package implements the tentaclio databricks+pyodbc database client"""

from tentaclio import *  # noqa

# fmt: off
from .clients.databricks_client import DatabricksClient


# Add DB registry
DB_REGISTRY.register("databricks+thrift", DatabricksClient)  # type: ignore
