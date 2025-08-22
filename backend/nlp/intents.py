from typing import Tuple
from ..models.enums import IntentName


# Toy keyword model. Replace with something smarter later.
_KEYWORDS = {
IntentName.admissions: ["admission", "apply", "deadline", "fees", "scholarship"],
IntentName.courses: ["course", "major", "minor", "credit", "syllabus"],
IntentName.schedules: ["schedule", "time", "timetable", "calendar"],
IntentName.events: ["event", "seminar", "workshop", "festival"],
}


def detect_intent(text: str) -> Tuple[IntentName, float]:
    t = text.lower()
    for intent, keys in _KEYWORDS.items():
        if any(k in t for k in keys):
            return intent, 0.8
        return IntentName.general, 0.5