# Document Matcher
### Scalable Semantic Search Engine (FastAPI + Sentence Transformers + FAISS)

A **semantic document retrieval system** that uses embeddings and FAISS for high-speed, low-latency similarity search.  
Containerized for deployment via **Docker**, built with **FastAPI**, and optimized for **real-time AI inference**.

---

## Overview
Document Matcher allows querying large text corpora and retrieving semantically similar results in sub-milliseconds using FAISS.  
It demonstrates backend scalability, containerized deployment, and ML system integration.

---

## Tech Stack
- **FastAPI** — RESTful backend  
- **Sentence Transformers** — embeddings  
- **FAISS (Facebook AI Similarity Search)** — vector indexing  
- **Docker + Uvicorn** — deployment  
- **PyTorch / NumPy / Pandas** — data + math  

---

## Setup
```bash
git clone https://github.com/triiJU/Document-Matcher.git
cd Document-Matcher
pip install -r requirements.txt
uvicorn app.main:app --reload
