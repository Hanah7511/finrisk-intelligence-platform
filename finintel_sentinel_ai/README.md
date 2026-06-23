finintel_sentinel_ai/README.md

# FinIntel Sentinel AI

> LangGraph multi-agent investigation system for financial crime analysis, regulatory reasoning, and automated SAR report generation.

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)

Part of the [Financial Risk Intelligence Platform](../README.md)

---

## Overview

FinIntel Sentinel AI receives alerts from the `finrisk_detection_engine` and autonomously investigates them using a team of specialized AI agents. It reasons over regulatory documents (FATF, FinCEN), scores confidence, and generates SAR reports.

---

## Agent Architecture

Alert Input
    │
    ▼
Investigation Agent  ──→  queries RAG pipeline, builds case timeline
    │
    ▼
Compliance Agent     ──→  maps findings to FATF / FinCEN regulations
    │
    ▼
Summarization Agent  ──→  generates SAR narrative and risk summary
    │
    ▼
SAR Report Output

---

## RAG Pipeline

- Regulatory documents loaded from FATF, FinCEN, internal policies
- Chunked and embedded using Sentence Transformers
- Stored in FAISS (fast similarity search) and ChromaDB (persistent store)
- Retrieved context passed to agents for grounded reasoning

---

## Tech Stack

| Layer | Technologies |
|---|---|
| Agent Framework | LangGraph, LangChain |
| LLM | OpenAI API |
| Vector Stores | FAISS, ChromaDB |
| Embeddings | Sentence Transformers |
| API | FastAPI |
| Infra | Docker |

---

## Folder Structure

finintel_sentinel_ai/
├── src/
│   ├── agents/              # investigation, compliance, summarization agents
│   ├── rag/                 # retrieval pipeline
│   ├── vector_store/        # FAISS and ChromaDB setup
│   ├── embeddings/          # embedding generation
│   ├── chunking/            # document chunking strategies
│   ├── confidence_scoring/  # response confidence scoring
│   ├── sar_generation/      # SAR drafting and narrative building
│   ├── reporting/           # final report export
│   └── api/                 # FastAPI service
├── configs/
├── notebooks/
├── tests/
└── README.md

---

## Status

| Component | Status |
|---|---|
| RAG Pipeline | In Progress |
| Investigation Agent | In Progress |
| Compliance Agent | In Progress |
| Summarization Agent | In Progress |
| SAR Generation | In Progress |

---

*Part of [Financial Risk Intelligence Platform](https://github.com/Hanah7511/finrisk-intelligence-platform)*

---
Paste the first one into your root README.md and the second into finintel_sentinel_ai/README.md. Then commit and push both.

✻ Baked for 26s

❯ how to do that

Here's exactly how:

---
Add the main README

Step 1 — Go to your GitHub repo: https://github.com/Hanah7511/finrisk-intelligence-platform

Step 2 — Click on Readme.md (you can see it in the file list)

Step 3 — Click the pencil icon (Edit) on the top right of the file

Step 4 — Select all the existing content and delete it

Step 5 — Paste the main README I gave you

Step 6 — Scroll down, click "Commit changes" → click "Commit changes" again

---
Add the finintel_sentinel_ai README

Step 1 — Go to your repo root page

Step 2 — Click into the finintel_sentinel_ai folder (if it exists) OR if it doesn't exist yet:
- Click "Add file" → "Create new file"
- In the filename box type: finintel_sentinel_ai/README.mdreports.

---

## Agent Architecture

Alert Input
    │
    ▼
Investigation Agent  ──→  queries RAG pipeline, builds case timeline
    │
    ▼
Compliance Agent     ──→  maps findings to FATF / FinCEN regulations
    │
    ▼
Summarization Agent  ──→  generates SAR narrative and risk summary
    │
    ▼
SAR Report Output

---

## RAG Pipeline

- Regulatory documents loaded from FATF, FinCEN, internal policies
- Chunked and embedded using Sentence Transformers
- Stored in FAISS (fast similarity search) and ChromaDB (persistent store)
- Retrieved context passed to agents for grounded reasoning

---

## Tech Stack

| Layer | Technologies |
|---|---|
| Agent Framework | LangGraph, LangChain |
| LLM | OpenAI API |
| Vector Stores | FAISS, ChromaDB |
| Embeddings | Sentence Transformers |
| API | FastAPI |
| Infra | Docker |

---

## Folder Structure

finintel_sentinel_ai/
├── src/
│   ├── agents/              # investigation, compliance, summarization agents
│   ├── rag/                 # retrieval pipeline
│   ├── vector_store/        # FAISS and ChromaDB setup
│   ├── embeddings/          # embedding generation
│   ├── chunking/            # document chunking strategies
│   ├── confidence_scoring/  # response confidence scoring
│   ├── sar_generation/      # SAR drafting and narrative building
│   ├── reporting/           # final report export
│   └── api/                 # FastAPI service
├── configs/
├── notebooks/
├── tests/
└── README.md

---

## Status

| Component | Status |
|---|---|
| RAG Pipeline | In Progress |
| Investigation Agent | In Progress |
| Compliance Agent | In Progress |
| Summarization Agent | In Progress |
| SAR Generation | In Progress |

---

*Part of [Financial Risk Intelligence Platform](https://github.com/Hanah7511/finrisk-intelligence-platform)*
