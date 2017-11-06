from __future__ import absolute_import

from ibis.pandas.client import PandasClient, PandasTable, pandas_dtypes_to_ibis_schema
from ibis.pandas.decimal import execute_node  # noqa: F401
from ibis.pandas.execution import execute  # noqa: F401


def connect(dictionary):
    return PandasClient(dictionary)
