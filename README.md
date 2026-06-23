# Financial Risk Intelligence Platform

> Enterprise-grade AML detection and financial crime investigation platform combining classical ML, Graph Neural Networks, and LangGraph multi-agent AI.

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This platform is built to detect financial crime at scale and investigate suspicious activity through autonomous AI agents. It combines a multi-layer ML detection pipeline with a LangGraph-powered investigation system, connected through a shared contract layer.

---

## Architecture

finrisk-intelligence-platform/
├── finrisk_detection_engine/     ⚙ AML Detection Pipeline
└── finintel_sentinel_ai/         🤖 Multi-Agent Investigation System

### ⚙ finrisk_detection_engine
Multi-layer AML detection pipeline:
- Rule-based detection (structuring, sanctions, velocity, geo-risk)
- Statistical anomaly detection — Z-score, IQR, MAD
- Ensemble ML — Isolation Forest, XGBoost, Random Forest
- GraphSAGE GNN for fraud ring detection
- Risk fusion engine combining all signals
- Real-time FastAPI scoring API with MLflow tracking and Docker deployment

### 🤖 finintel_sentinel_ai
LangGraph multi-agent investigation system:
- Investigation Agent, Compliance Agent, Summarization Agent
- RAG pipeline over FATF and FinCEN regulatory documents
- Vector stores: FAISS + ChromaDB
- Confidence scoring and automated SAR report generation

---

## Pipeline Flow

SQL Ingest → Validate → Preprocess → Features → Rules → Stat ML → XGBoost → GNN → Fusion → Alert → SAR Report

---

## Tech Stack

| Layer | Technologies |
|---|---|
| ML & Deep Learning | Python, XGBoost, PyTorch, GraphSAGE, NetworkX, Scikit-learn |
| Agentic AI | LangGraph, LangChain, OpenAI API |
| Vector / RAG | FAISS, ChromaDB, Sentence Transformers |
| API & Infra | FastAPI, MLflow, Docker, GitHub Actions |
| Data | SQL Server, Pandas |

---

## Repo Structure

finrisk-intelligence-platform/
├── shared/
│   ├── schemas/
finrisk-intelligence-platform/
├── shared/
│   ├── schemas/
│   ├── configs/
│   ├── utils/
│   └── contracts/
├── finrisk_detection_engine/
│   ├── src/
│   ├── configs/
│   ├── notebooks/
│   └── tests/
│   ├── configs/
│   ├── notebooks/
│   └── tests/
├── finintel_sentinel_ai/
│   ├── src/
│   ├── configs/
│   ├── notebooks/
│   └── tests/
├── data/
├── docs/
├── docker-compose.yml
└── README.md

---

## Status

| Component | Status |
|---|---|
| finrisk_detection_engine | In Progress |
| finintel_sentinel_ai | In Progress |

---

*Built by [Hana Al Haris](https://github.com/Hanah7511)*
