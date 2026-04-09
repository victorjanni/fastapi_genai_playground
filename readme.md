# 🚀 FastAPI GenAI Playground

A hands-on playground to learn and build **FastAPI backend systems**, **CRUD APIs**, and extend into **GenAI / AI engineering**.

This project is designed to help you move from:

* Basic API development
  ➡️ To
* Real-world AI backend architecture

---

# 📌 Overview

This repository includes:

* ✅ FastAPI CRUD project (Employee Management)
* ✅ SQLAlchemy ORM integration
* ✅ Pydantic schemas
* ✅ SQLite database
* 🔜 Future GenAI integrations (OpenAI, LangChain, RAG, Agents)

---

# 🧱 Project Structure

```bash
fastapi_genai_playground/
│
├── Database Integration/
│   └── crud_app/
│       ├── main.py
│       ├── crud.py
│       ├── models.py
│       ├── schemas.py
│       ├── database.py
│       └── employees.db
│
├── myenv/
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn

---

# 🛠️ Setup Instructions

## 1. Clone the repository

```bash
git clone <your-repo-url>
cd fastapi_genai_playground
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

## 3. Install dependencies

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic email-validator
```

---

# ▶️ Run the Application

Navigate to CRUD app:

```bash
cd "Database Integration/crud_app"
```

Start server:

```bash
uvicorn main:app --reload
```

---

# 🌐 API Access

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

# 📡 API Endpoints

## 🔹 Create Employee

**POST** `/employees`

```json
{
  "name": "Victor",
  "email": "victor@gmail.com",
  "department": "AI"
}
```

---

## 🔹 Get All Employees

**GET** `/employees`

---

## 🔹 Get Employee by ID

**GET** `/employees/{emp_id}`

---

# 🧠 Core Files Explained

## `main.py`

* FastAPI app
* API routes
* Dependency injection

## `database.py`

* DB connection
* Engine setup
* Session management

## `models.py`

* SQLAlchemy table definitions

## `schemas.py`

* Pydantic request/response models

## `crud.py`

* Database logic (Create, Read operations)

---

# ✅ Features Implemented

* [x] Create Employee
* [x] Get All Employees
* [x] Get Employee by ID
* [ ] Update Employee
* [ ] Delete Employee

---

# 🎯 Learning Goals

This project helps you learn:

* FastAPI backend development
* REST API design
* Database integration
* Clean architecture (routes → services → DB)
* Debugging real backend issues
* Preparing for AI backend systems

---

# 🔮 Future Roadmap

* [ ] Update & Delete APIs
* [ ] PostgreSQL integration
* [ ] JWT Authentication
* [ ] File Upload APIs
* [ ] OpenAI Integration
* [ ] LangChain / LangGraph
* [ ] RAG pipeline
* [ ] Redis + Background workers
* [ ] React frontend integration

---

# 📝 Notes

This is not just a tutorial project.

It is a **growing AI backend playground** aimed at:

* real-world backend skills
* AI system design
* startup-level architecture


