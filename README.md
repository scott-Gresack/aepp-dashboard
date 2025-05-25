# AEPP Use Case Dashboard

A full-stack application for monitoring and interacting with Adobe Experience Platform Privacy (AEPP) and related Adobe Experience Cloud services using FastAPI and Vue 3.

---

## 📁 Project Structure

```
aepp_dashboard_final/
├── backend/                  # FastAPI backend
│   ├── main.py               # App entry point
│   ├── agents.py             # AEPP monitoring agent
│   └── routers/              # Organized API routes
│       ├── web_analytics.py
│       ├── ajo_insights.py
│       └── aepp.py
│
├── frontend/
│   └── src/components/
│       └── App.vue           # Vue frontend UI
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Backend Setup (Python 3.10+)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn httpx
uvicorn main:app --reload
```

### 2. Frontend Setup (Vue 3)
```bash
cd frontend
npm install
npm run dev
```

---

## 🧩 Supported Use Cases

### 📊 Web Analytics (Explore 201)
- Count events
- Track unique visitors
- Page view metrics

### ✨ Adobe Journey Optimizer (Explore 300)
- Schema exploration
- Journey structure

### 🔐 AEPP Operations
- Fetch & manage schemas, datasets
- Update Data Prep
- Modify Datastreams
- Execute SQL Queries
- View Audiences, Journeys, and Profiles

### 📡 Monitoring Agents
- Run live health checks on AEPP endpoints
- Return structured service logs via `/api/aepp/agents/monitor`

---

## 📈 Visualization Layer

Real-time charts and logs:
- Web metrics chart (event/session)
- Log console from agents
- Organizational tree-style graph for AEPP structure (in dev)

---

## 🔐 Environment Config

Configure `.env` or set directly in agent and API service:

```
ADOBE_CLIENT_ID=
ADOBE_CLIENT_SECRET=
ADOBE_ORG_ID=
ADOBE_TECHNICAL_ACCOUNT_ID=
ADOBE_PRIVATE_KEY_PATH=
```

---

## 🙋‍♂️ Author

Built by Scott Gresack — martech engineer & data instrumentation lead.