"""This package implements the tentaclio databricks database client"""

from importlib.metadata import version as _version

from tentaclio import *  # noqa

from .clients.databricks_client import DatabricksClient

__version__ = _version("tentaclio-databricks")

# Add DB registry
DB_REGISTRY.register("databricks+thrift", DatabricksClient)  # type: ignore
