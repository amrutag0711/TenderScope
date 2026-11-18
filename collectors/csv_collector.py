"""COLLECTOR: reads user-uploaded CSV/Excel files and passes them to preprocessing."""

import pandas as pd
from preprocessing.cleaning import preprocess


def read_table(file, name=''):
    """Read CSV/XLSX into a raw DataFrame; CSV falls back to latin-1 if not UTF-8."""
    if str(name or getattr(file, 'name', '')).lower().endswith(('.xlsx', '.xls')):
        return pd.read_excel(file)
    try:
        return pd.read_csv(file)
    except UnicodeDecodeError:
        if hasattr(file, 'seek'):
            file.seek(0)
        return pd.read_csv(file, encoding='latin-1')


def import_csv(file):
    return preprocess(read_table(file, 'x.csv'))


def import_excel(file):
    return preprocess(pd.read_excel(file))
