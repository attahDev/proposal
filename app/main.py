from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers import proposals

app = FastAPI(
    title="Proposal Builder",
    description="NL prompt → structured business proposal → PDF/DOCX",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proposals.router)

ui_dir = Path(__file__).parent.parent / "ui"
app.mount("/", StaticFiles(directory=str(ui_dir), html=True), name="ui")
