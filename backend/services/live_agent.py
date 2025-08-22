from ..models.schemas import ChatRequest


async def should_handoff(_: ChatRequest) -> bool:
    return False