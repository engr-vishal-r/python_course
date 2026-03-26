from google.cloud import bigquery
import pandas as pd
from datetime import datetime


def write_schema_drift(table, extra_columns, missing_columns):
    if not extra_columns and not missing_columns:
        return

    client = bigquery.Client()

    rows = []

    for col in extra_columns:
        rows.append({
            "table_name": table,
            "column_name": col,
            "issue_type": "EXTRA_COLUMN",
            "detected_at": datetime.utcnow()
        })

    for col in missing_columns:
        rows.append({
            "table_name": table,
            "column_name": col,
            "issue_type": "MISSING_COLUMN",
            "detected_at": datetime.utcnow()
        })

    pdf = pd.DataFrame(rows)

    client.load_table_from_dataframe(
        pdf,
        "metadata.schema_drift"
    ).result()