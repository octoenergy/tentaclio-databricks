import pytest
from tentaclio import URL

from tentaclio_databricks.clients.databricks_client import DatabricksClient


@pytest.mark.parametrize(
    "url, server_hostname, http_path, access_token",
    [
        (
            "databricks+thrift://my_t0k3n@host.databricks.com"
            "?HTTPPath=/sql/1.0/endpoints/123456789",
            "host.databricks.com",
            "/sql/1.0/endpoints/123456789",
            "my_t0k3n",
        ),
        (
            "databricks+thrift://my_t0k3n@host.databricks.com:443/"
            "?HTTPPath=/sql/1.0/endpoints/123456789"
            "&AuthMech=3&SparkServerType=3&ThriftTransport=2&SSL=1&"
            "IgnoreTransactions=1&DRIVER=/Library/simba/spark/lib/libsparkodbc_sbu.dylib",
            "host.databricks.com",
            "/sql/1.0/endpoints/123456789",
            "my_t0k3n",
        ),
    ],
)
def test_build_odbc_connection_dict(url, server_hostname, http_path, access_token):
    client = DatabricksClient(URL(url))
    assert client.server_hostname == server_hostname
    assert client.http_path == http_path
    assert client.access_token == access_token
