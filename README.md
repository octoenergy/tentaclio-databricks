
# tentaclio-databricks

A package containing all the dependencies for the `databricks+thrift` tentaclio schema .

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

Your connection url should be in the following format:

```
databricks+thrift://<token>@<host>?HTTPPath=<http_path>
```

Example values:
- token: dapi1213456789abc
- host: myhost.databricks.com
- http_path: /sql/1.0/endpoints/123456789