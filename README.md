# Document_Matcher

A scalable document retrieval system that matches user queries with semantically similar documents using **Sentence Transformers** and **FastAPI**.

---

## Overview
This project provides an intelligent backend service that allows querying large document collections for semantic similarity.  
Built for modularity, performance, and deployability.

---

## Tech Stack
- **FastAPI** — API framework  
- **Sentence Transformers** — embedding generation  
- **PyTorch / NumPy** — vector computations  
- **Docker** — containerized deployment  
- **Uvicorn** — ASGI server  

---

## Setup
```bash
git clone https://github.com/triiJU/Document-Matcher.git
cd Document-Matcher
pip install -r requirements.txt
uvicorn app.main:app --reload
