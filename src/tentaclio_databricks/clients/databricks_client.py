"""Databricks query client."""
import pandas as pd
import pyarrow as pa
from databricks import sql
from databricks.sql.types import Row
from tentaclio import URL


class DatabricksClientException(Exception):
    """Databricks client specific exception."""


class DatabricksClient:
    """Databricks client, backed by an Apache Thrift connection."""

    def __init__(self, url: URL, arraysize: int = 1000000, **kwargs):

        # This is a very common issue reported by the users
        if url.query is None or "HTTPPath" not in url.query:
            raise DatabricksClientException(
                "Missing the HTTPPath element in the http query. \n\n"
                "The url should look like: "
                "databricks+thrift://workspaceurl.databricks.com/?HTTPPath=value\n"
                "Check the connection details of your databricks warehouse"
            )
        if url.username is None or url.username == "":
            raise DatabricksClientException(
                "Missing the token in the url:\n\n"
                "The url should look like: "
                "databricks+thrift://token@workspaceurl.databricks.com/?HTTPPath=value"
            )

        self.server_hostname = url.hostname
        self.http_path = url.query["HTTPPath"]
        self.access_token = url.username
        self.arraysize = arraysize

    def __enter__(self):
        self.conn = sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token,
        )
        self.cursor = self.conn.cursor(arraysize=self.arraysize)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cursor.close()

    def query(self, sql_query: str, **kwargs) -> list[Row]:
        """Execute a SQL query, and return results."""
        self.cursor.execute(sql_query, **kwargs)
        return self.cursor.fetchall()

    def execute(self, sql_query: str, **kwargs) -> None:
        """Execute a raw SQL query command."""
        self.cursor.execute(sql_query, **kwargs)

    def get_df(self, sql_query: str, **kwargs) -> pd.DataFrame:
        """Run a raw SQL query and return a data frame."""
        data = self.query(sql_query, **kwargs)
        columns = [col_desc[0] for col_desc in self.cursor.description]
        return pd.DataFrame(data, columns=columns)
    
    def get_arrow_table(self, sql_query: str, **kwargs) -> pa.Table:
        """Run a raw SQL query and return a `pyarrow.Table`."""
        self.cursor.execute(sql_query, **kwargs)
        return self.cursor.fetchall_arrow()
