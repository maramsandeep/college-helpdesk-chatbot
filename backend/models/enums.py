from enum import Enum


class Channel(str, Enum):
    web = "web"
    whatsapp = "whatsapp"
    telegram = "telegram"


class IntentName(str, Enum):
    general = "general"
    admissions = "admissions"
    courses = "courses"
    schedules = "schedules"
    events = "events"
    unknown = "unknown"