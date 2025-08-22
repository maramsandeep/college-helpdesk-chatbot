from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict, Any
from datetime import datetime
from .enums import Channel, IntentName


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)


class ChatRequest(BaseModel):
    session_id: str
    message: str
    channel: Channel = Channel.web


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    intent: IntentName = IntentName.general
    handoff: bool = False


class WebhookEvent(BaseModel):
    provider: str
    event_type: str
    payload: Dict[str, Any] = {}