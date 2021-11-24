"""The client module defines stream and query based clients.

Stream clients allow to read and write from stream based sources with ease,
and in an interchangable manner.

Query based clients unify how to access databases leveraging from sqlalchemy.
"""

from .databricks_client import *  # noqa
