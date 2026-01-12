from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import upload, query, reports, health, auth
from .routers.ingest import router as ingest_router




app = FastAPI(title="MagicBus AI Analytics Agent", version="1.0")

# CORS — allow your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(upload.router, prefix="/api")
app.include_router(query.router, prefix="/api")
app.include_router(reports.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(ingest_router)

@app.get("/")
def root():
    return {"message": "MagicBus AI Analytics Agent Backend Running"}
