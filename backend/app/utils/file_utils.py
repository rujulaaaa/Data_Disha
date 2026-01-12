import os
from fastapi import UploadFile

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_uploaded_file(upload_file: UploadFile, upload_dir: str) -> str:
    ensure_dir(upload_dir)
    dest_path = os.path.join(upload_dir, upload_file.filename)
    with open(dest_path, "wb") as f:
        content = upload_file.file.read()
        f.write(content)
    return dest_path