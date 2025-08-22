from fastapi import APIRouter, Depends, Request
from ..models.schemas import WebhookEvent
from ..core.db import get_db


router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


@router.post("/provider")
async def handle_provider(event: WebhookEvent, request: Request, db = Depends(get_db)):
    await db.webhooks.insert_one(event.model_dump())
    return {"status": "ok"}