from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from ..core.db import get_db


router = APIRouter(tags=["admin"])
_templates = Jinja2Templates(directory="dashboard/templates")


@router.get("/admin")
async def admin_page(request: Request, db = Depends(get_db)):
    msg_count = await db.messages.count_documents({})
    users = await db.messages.distinct("session_id")
    return _templates.TemplateResponse(
        "admin.html",
        {"request": request, "msg_count": msg_count, "user_count": len(users)}
)