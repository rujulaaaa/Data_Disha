from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import pandas as pd
import shutil

# Import the indexer
from ..core.data_indexer import index_data

router = APIRouter(prefix="/api")

# Path to uploads
UPLOAD_DIR = Path("backend/app/storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # 1. Save file
    save_path = UPLOAD_DIR / file.filename
    with save_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    # 2. INGEST FILE (THIS WAS MISSING)
    try:
        if save_path.suffix.lower() == ".csv":
            df = pd.read_csv(save_path)
            index_data({"sheet1": df}, file_name=save_path.stem)

        elif save_path.suffix.lower() in [".xlsx", ".xls"]:
            sheets = pd.read_excel(save_path, sheet_name=None)
            index_data(sheets, file_name=save_path.stem)

        else:
            return {"status": "saved", "detail": "File uploaded but not indexed (unsupported type)."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

    return {"status": "success", "file": file.filename, "indexed": True}
