"""Databricks query client."""
from typing import List

import pandas as pd
from databricks import sql
from tentaclio import URL


class DatabricksClient:
    """Databricks client, backed by an Apache Thrift connection."""

    def __init__(self, url: URL, **kwargs):
        self.server_hostname = url.hostname
        self.http_path = url.query["HTTPPath"]
        self.access_token = url.username

    def __enter__(self):
        self.conn = sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token,
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cursor.close()

    def query(self, sql_query: str, **kwargs) -> List[tuple]:
        """Execute a SQL query, and return results."""
        self.cursor.execute(sql_query, **kwargs)
        return self.cursor.fetchall()

    def execute(self, sql_query: str, **kwargs) -> None:
        """Execute a raw SQL query command."""
        self.cursor.execute(sql_query, **kwargs)

    def get_df(self, sql_query: str, params: dict = None, **kwargs) -> pd.DataFrame:
        """Run a raw SQL query and return a data frame."""
        return pd.read_sql(sql_query, self.conn, params=params, **kwargs)
