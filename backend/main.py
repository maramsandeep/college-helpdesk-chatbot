from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
import pathlib

from backend.core.config import settings
from backend.routes import chat, webhooks, admin

FRONTEND_DIR = pathlib.Path(__file__).parent.parent / "frontend"

app = FastAPI(title=settings.app_name)

# Static files
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/")
def root():
    return {"message": "College Helpdesk Chatbot backend is running!"}

# Routers
app.include_router(chat.router)         # chat already has prefix="/api"
app.include_router(webhooks.router)     # check if you added prefix there
app.include_router(admin.router)        # check if you added prefix there
