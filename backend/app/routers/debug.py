# backend/app/routers/debug.py
from fastapi import APIRouter
from ..core.data_indexer import TABLE_REGISTRY, METADATA

router = APIRouter(prefix="/api")

@router.get("/tables/")
def list_tables():
    return {"tables": list(TABLE_REGISTRY.keys()), "metadata_count": len(METADATA)}
