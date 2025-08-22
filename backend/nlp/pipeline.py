from .intents import detect_intent
from .retrieval import retrieve_answer
from ..models.enums import IntentName


class NLPResult:
    def __init__(self, intent: IntentName, answer: str):
        self.intent = intent
        self.answer = answer


async def process_message(text: str) -> NLPResult:
    intent, _ = detect_intent(text)
    answer = retrieve_answer(intent)
    return NLPResult(intent, answer)