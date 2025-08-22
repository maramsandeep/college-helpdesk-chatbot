from fastapi import APIRouter, Depends, Request
from ..models.schemas import ChatRequest, ChatResponse
from ..services.orchestrator import Orchestrator
from ..core.db import get_db


router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, request: Request, db = Depends(get_db)):
    orch = Orchestrator(db)
    return await orch.handle_chat(req)