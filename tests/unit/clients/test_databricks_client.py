import pandas as pd
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
            "databricks+thrift://p@ssw0rd@host.databricks.co.uk"
            "?HTTPPath=/sql/1.0/endpoints/987654321",
            "host.databricks.co.uk",
            "/sql/1.0/endpoints/987654321",
            "p@ssw0rd",
        ),
    ],
)
def test_build_connection_dict(url, server_hostname, http_path, access_token):
    client = DatabricksClient(URL(url))
    assert client.server_hostname == server_hostname
    assert client.http_path == http_path
    assert client.access_token == access_token


def test_get_df(mocker):
    expected = pd.DataFrame({"id": [1, 2, 3]})
    url = "databricks+thrift://my_t0k3n@host.databricks.com?HTTPPath=/sql/1.0/endpoints/123456789"
    client = DatabricksClient(URL(url))
    client.__enter__ = lambda _: client  # type: ignore
    client.query = lambda _: [1, 2, 3]  # type: ignore
    client.cursor = mocker.MagicMock()
    client.cursor.description = [("id", "int", None)]
    df = client.get_df("foo")
    assert df.equals(expected)
