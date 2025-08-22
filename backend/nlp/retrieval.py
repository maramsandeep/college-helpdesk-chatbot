from ..models.enums import IntentName


_FAQ = {
IntentName.admissions: "Admissions open year-round. Deadlines vary by program. Check the admissions page for specifics.",
IntentName.courses: "You can browse courses in the catalog. Popular picks: CS101, MATH201, ENG150.",
IntentName.schedules: "Semester starts Aug 26. Final exam window is Dec 9–13. See the academic calendar.",
IntentName.events: "This month: orientation week, hackathon, and alumni meetup.",
IntentName.general: "Ask me about admissions, courses, schedules, or campus events.",
}


def retrieve_answer(intent: IntentName) -> str:
    return _FAQ.get(intent, _FAQ[IntentName.general])