"""Automated tests (pytest) for preprocessing, algorithms, parser, database and exports."""

import pandas as pd
from preprocessing.cleaning import preprocess, money, clean_text
from mining.analytics import associations, similar, cluster, search, trends
from collectors.local_html import parse_local_html
from config import SAMPLE


def data():
    return preprocess(pd.read_csv(SAMPLE).head(100))


def test_money():
    assert money('2 lakh') == 200000 and money('1.5 crore') == 15000000


def test_clean():
    assert 'comput' in clean_text('Computers and equipment!')


def test_dedup():
    d = pd.DataFrame(
        {'tender_id': ['a', 'a'], 'tender_title': ['one', 'two'], 'source_portal': ['x', 'x']}
    )
    assert len(preprocess(d)) == 1


def test_missing_required():
    import pytest

    with pytest.raises(ValueError):
        preprocess(pd.DataFrame({'bad': [1]}))


def test_algorithms():
    d = data()
    assert not search(d, 'solar').empty
    assert len(similar(d, 0)) > 0
    out, names, metrics = cluster(d, 3)
    assert len(out) == len(d) and len(names) == 3
    items, rules = associations(d, 0.02, 0.2)
    assert not items.empty
    assert not trends(d).empty


def test_html():
    assert (
        len(
            parse_local_html(
                '<table><tr data-tender-id="1"><td>Title</td><td>Office</td></tr></table>'
            )
        )
        == 1
    )


def test_db_roundtrip(tmp_path, monkeypatch):
    import importlib, config

    monkeypatch.setenv('TENDERSCOPE_DB', str(tmp_path / 't.sqlite'))
    importlib.reload(config)
    import database.db as db

    importlib.reload(db)
    d = data().head(20)
    db.store(d, 'test')
    back = preprocess(db.load())
    assert len(back) == len(d)
    assert back.tender_description.astype(str).ne('<NA>').all()
    db.store(d, 'again')
    assert len(db.load()) == len(d)  # upsert, no duplicates


def test_csv_encoding_fallback():
    from io import BytesIO
    from collectors.csv_collector import read_table

    f = BytesIO('tender_id,tender_title\n1,Caf\xe9 supplies\n'.encode('latin-1'))
    assert len(read_table(f, 'x.csv')) == 1


def test_excel_formula_sanitized():
    from utils.exports import _safe

    assert _safe('=1+1').startswith("'") and _safe('ok') == 'ok'
