# 🎓 College Helpdesk Chatbot

An **AI-powered chatbot** for handling college helpdesk queries such as admissions, course offerings, schedules, and campus events.  
Built with **FastAPI**, **MongoDB**, and a simple **NLP pipeline**. Includes a lightweight web frontend and an admin dashboard.

---

## 🚀 Features
- FastAPI backend with modular routes
- MongoDB integration using Motor (async driver)
- Simple keyword-based intent detection
- Retrieval-based FAQ answers
- REST API for chatbot interactions
- Webhooks endpoint (for future integrations like WhatsApp/Telegram)
- Minimal web frontend (HTML, CSS, JS)
- Admin dashboard with session/message stats

---

## 📂 Project Structure
```

.
├── README.md
├── backend
│   ├── main.py                # FastAPI entrypoint
│   ├── core
│   │   ├── config.py           # Settings loader
│   │   └── db.py               # MongoDB connection
│   ├── models
│   │   ├── enums.py            # Enums (Intent, Channel)
│   │   └── schemas.py          # Pydantic models
│   ├── nlp
│   │   ├── intents.py          # Intent detection
│   │   ├── retrieval.py        # FAQ retrieval
│   │   └── pipeline.py         # NLP pipeline
│   ├── services
│   │   ├── orchestrator.py     # Orchestrates NLP + DB
│   │   └── live\_agent.py       # Stub for live agent handoff
│   └── routes
│       ├── chat.py             # /api/chat endpoint
│       ├── webhooks.py         # /api/webhooks/provider
│       └── admin.py            # /admin dashboard
├── frontend
│   ├── index.html              # Chat UI
│   ├── app.js                  # Chat logic (fetch API)
│   └── styles.css              # Styling
└── dashboard
└── templates
└── admin.html          # Admin dashboard template

````

---

## ⚙️ Requirements
- Python 3.10+
- MongoDB (local or remote instance)
- Node not required (frontend is plain HTML/JS/CSS)

---

## 🔧 Installation

Clone the repo:
```bash
git clone https://github.com/<your-username>/college-helpdesk-chatbot.git
cd college-helpdesk-chatbot
````

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows
```

Install dependencies:

```bash
pip install fastapi "uvicorn[standard]" motor pydantic jinja2
```

---

## ⚡ Running the App

Make sure MongoDB is running locally (or update `MONGO_URI`).

Start the app:

```bash
uvicorn backend.main:app --reload
```

If port 8000 is already in use:

```bash
uvicorn backend.main:app --reload --port 8001
```

---

## 🌐 Usage

### Web UI

* Open [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Type a message in the chat window

### API Docs

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Admin Dashboard

* [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📡 Example API Calls

Chat with the bot:

```bash
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "demo123",
    "message": "When does the semester start?",
    "channel": "web"
  }'
```

Webhook event:

```bash
curl -X POST http://127.0.0.1:8000/api/webhooks/provider \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "whatsapp",
    "event_type": "message",
    "payload": { "text": "Hello" }
  }'
```

---

## ⚙️ Environment Variables

| Variable    | Default                     | Description            |
| ----------- | --------------------------- | ---------------------- |
| `MONGO_URI` | `mongodb://localhost:27017` | MongoDB connection URI |
| `DB_NAME`   | `helpdesk_db`               | MongoDB database name  |

Example:

```bash
export MONGO_URI="mongodb://localhost:27017"
export DB_NAME="college_helpdesk"
```

---

## 📊 Data Storage

* `messages` collection → Stores all chat history (user + bot)
* `webhooks` collection → Stores incoming webhook events

---

## 🛠️ Next Steps

* Replace toy NLP with a real model (transformers, RAG, or LangChain)
* Integrate WhatsApp/Telegram APIs in `routes/webhooks.py`
* Add live agent support in `services/live_agent.py`
* Deploy to cloud (Render, Railway, or AWS)

---

## 📜 License

MIT – free to use, modify, and share.

```

---

