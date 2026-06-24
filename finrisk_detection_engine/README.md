# FinRisk Detection Engine

> Multi-layer AML detection pipeline combining rule-based engines, statistical anomaly detection, ensemble ML, and Graph Neural Networks for real-time financial crime scoring.

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble%20ML-green)

Part of the [Financial Risk Intelligence Platform](../README.md)

---

## Overview

The `finrisk_detection_engine` is the detection backbone of the Financial Risk Intelligence Platform. It ingests raw transaction data, applies multiple detection layers, fuses risk signals, and generates alerts that are passed to `finintel_sentinel_ai` for autonomous investigation.

---

## Detection Pipeline

SQL Ingest → Validate → Preprocess → Feature Engineering
    │
    ▼
Rule-Based Engine     ──→  structuring, sanctions, velocity, geo-risk
    │
    ▼
Statistical Detection ──→  Z-score, IQR, MAD anomaly detection
    │
    ▼
Ensemble ML           ──→  Isolation Forest, XGBoost, Random Forest
    │
    ▼
GNN Layer             ──→  GraphSAGE fraud ring detection
    │
    ▼
Risk Fusion Engine    ──→  combines all signals into a unified risk score
    │
    ▼
Alert → SAR Report

---

## Tech Stack

| Layer | Technologies |
|---|---|
| ML & Deep Learning | Python, XGBoost, PyTorch, GraphSAGE, NetworkX, Scikit-learn |
| API & Serving | FastAPI |
| Experiment Tracking | MLflow |
| Infrastructure | Docker, GitHub Actions |
| Data | SQL Server, Pandas |

---

## Folder Structure

finrisk_detection_engine/
├── src/
│   ├── ingestion/           # SQL data ingestion
│   ├── preprocessing/       # validation and feature engineering
│   ├── rules/               # rule-based detection engine
│   ├── statistical/         # Z-score, IQR, MAD detectors
│   ├── ml_models/           # Isolation Forest, XGBoost, RF
│   ├── gnn/                 # GraphSAGE fraud ring detection
│   ├── fusion/              # risk signal fusion engine
│   └── api/                 # FastAPI scoring endpoint
├── configs/
└── main.py

---

## Status

| Component | Status |
|---|---|
| Rule-Based Engine | In Progress |
| Statistical Detection | In Progress |
| Ensemble ML | In Progress |
| GNN (GraphSAGE) | In Progress |
| Risk Fusion | In Progress |
| FastAPI Scoring API | In Progress |

---

*Part of [Financial Risk Intelligence Platform](https://github.com/Hanah7511/finrisk-intelligence-platform)*
