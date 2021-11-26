
# tentaclio-databricks

A package containing all the dependencies for the `databricks+pyodbc` tentaclio schema .

## Quick Start

This project comes with a `Makefile` which is ready to do basic common tasks

```
$ make help
install                       Initalise the virtual env installing deps
clean                         Remove all the unwanted clutter
lock                          Lock dependencies
update                        Update dependencies (whole tree)
sync                          Install dependencies as per the lock file
lint                          Lint files with flake and mypy
format                        Run black and isort
test                          Run unit tests
circleci                      Validate circleci configuration (needs circleci cli)
```

## Configuring access to Databricks

In order to use Tentaclio to connect to a Databricks cluster or SQL endpoint, it is necessary to install the required
[ODBC driver](https://databricks.com/spark/odbc-drivers-download) for your operating system.

Once installed, it is possible to access Databricks as you would any supported URL protocol. However,
it is likely that you will have to pass some [additional variables](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html)
in the URL query string, including the path to the installed driver.

For example, if your Databricks connection requires you to set DRIVER and HTTPPATH values,
the URL should look like this:

```
databricks+pyodbc://<token>@<host>/<database>?DRIVER=<path/to/driver>&HTTPPath=<http_path>
```
