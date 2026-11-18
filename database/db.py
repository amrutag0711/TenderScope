"""DATABASE: saves and loads tender records using SQLite through SQLAlchemy."""

import json
from datetime import datetime, timezone
import pandas as pd
from sqlalchemy import create_engine, text
from config import DB

DB.parent.mkdir(parents=True, exist_ok=True)
engine = create_engine('sqlite:///' + str(DB))


def initialize():
    """Create the SQLite tables if they do not exist."""
    with engine.begin() as con:
        con.execute(
            text(
                'CREATE TABLE IF NOT EXISTS tenders (source_portal TEXT NOT NULL, tender_id TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY(source_portal,tender_id))'
            )
        )
        con.execute(
            text(
                'CREATE TABLE IF NOT EXISTS collection_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, message TEXT)'
            )
        )
        con.execute(
            text(
                'CREATE TABLE IF NOT EXISTS dataset_imports (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, source TEXT, records INTEGER)'
            )
        )
        con.execute(
            text('CREATE TABLE IF NOT EXISTS tender_keywords (tender_id TEXT, keyword TEXT)')
        )
        con.execute(
            text('CREATE TABLE IF NOT EXISTS tender_categories (category TEXT PRIMARY KEY)')
        )


def store(df, source='upload'):
    """Persist records (one JSON payload per tender). Missing values/dates become JSON null."""
    initialize()
    records = json.loads(df.to_json(orient='records', date_format='iso'))
    rows = [
        {'s': str(r['source_portal']), 'i': str(r['tender_id']), 'p': json.dumps(r)}
        for r in records
    ]
    with engine.begin() as con:
        if rows:
            con.execute(
                text(
                    'INSERT OR REPLACE INTO tenders(source_portal,tender_id,payload) VALUES (:s,:i,:p)'
                ),
                rows,
            )
        con.execute(
            text('INSERT INTO dataset_imports(timestamp,source,records) VALUES (:t,:s,:n)'),
            {'t': datetime.now(timezone.utc).isoformat(), 's': source, 'n': len(df)},
        )


def load():
    """Read all saved tenders back into a DataFrame."""
    initialize()
    with engine.connect() as con:
        rows = con.execute(text('SELECT payload FROM tenders')).fetchall()
    return pd.DataFrame([json.loads(r[0]) for r in rows])
