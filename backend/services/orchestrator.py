from ..models.schemas import ChatRequest, ChatResponse, ChatMessage
from ..nlp.pipeline import process_message
from .live_agent import should_handoff
from datetime import datetime


class Orchestrator:
    def __init__(self, db):
        self.db = db

    async def handle_chat(self, req: ChatRequest) -> ChatResponse:
        # persist inbound
        await self.db.messages.insert_one({
            "session_id": req.session_id,
            "role": "user",
            "content": req.message,
            "channel": req.channel.value,
            "ts": datetime.utcnow(),
        })

        # run handoff or NLP
        handoff = await should_handoff(req)
        if handoff:
            reply = "Connecting you to a live agent."
            intent = "general"
        else:
            nlp = await process_message(req.message)
            reply = nlp.answer
            intent = nlp.intent.value

        # persist outbound
        await self.db.messages.insert_one({
            "session_id": req.session_id,
            "role": "assistant",
            "content": reply,
            "ts": datetime.utcnow(),
        })

        return ChatResponse(
            session_id=req.session_id,
            reply=reply,
            intent=intent,
            handoff=handoff,
        )
