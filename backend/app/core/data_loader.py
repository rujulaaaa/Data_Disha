import pandas as pd
import tabula
import os

def load_raw_data(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        return { "default": pd.read_csv(file_path) }

    if ext in [".xls", ".xlsx"]:
        sheets = pd.read_excel(file_path, sheet_name=None)
        return sheets

    if ext == ".pdf":
        tables = tabula.read_pdf(file_path, pages="all", multiple_tables=True)
        return {f"table_{i}": t for i, t in enumerate(tables)}

    raise ValueError("Unsupported file format")
