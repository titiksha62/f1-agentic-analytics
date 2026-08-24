# 🏎️ Enterprise F1 Racing Intelligence Platform

An AI-powered analytics platform demonstrating a multi-tier agentic architecture, built on Google Cloud. 

This project orchestrates document retrieval, no-code agent workflows, and a code-first Agent Development Kit (ADK) to process 70+ years of Formula 1 telemetry, historical race data, and FIA regulations. 

## 🧠 The Core Philosophy: Agents are Data Controllers

The fundamental challenge in enterprise AI isn't the model's intelligence; it's matching the right data architecture to the right query type. This platform demonstrates that AI capability is determined by the data architecture underneath it. It solves this by separating concerns into three distinct tiers of data access, all powered by Gemini but utilizing fundamentally different underlying architectures.

---

## 🏗️ Architecture Overview

The platform serves three distinct audiences inside a racing organization, providing the right tier of data access to the right team member:

### 1. The Strategy Team: Retrieval Layer (RAG)
* **The Need:** Fast, accurate answers regarding parc fermé rules, penalties, and modifications.
* **The Architecture:** A Gemini Enterprise App grounded in official 2025/2026 FIA regulatory PDFs.
* **The Capability:** Searching unstructured data by meaning. Delivers cited, hallucination-free rule interpretations where source provenance is strictly maintained.

### 2. The Race Engineers: Orchestration Layer
* **The Need:** Comprehensive pre-race briefings synthesizing rules, circuit history, and current driver form.
* **The Architecture:** A multi-agent system built with Agent Designer. 
* **The Capability:** Orchestrates across multiple sources—proprietary driver profiles in BigQuery data stores, real-time web data, and FIA regulations—to assemble structured, cross-domain intelligence.

### 3. The Data Science Team: Computation Layer
* **The Need:** Predicted podium probabilities, statistical aggregations, and custom data visualizations.
* **The Architecture:** A code-first Python agent built using the **Agent Development Kit (ADK)**.
* **The Capability:** Connects directly to BigQuery to generate and execute live SQL, runs ML predictions, and writes Python code in isolated sandboxes to generate charts.

---

## ⚡ Key Technical Highlights

* **BigQuery ML (BQML):** Trained a logistic regression model entirely in SQL to predict podium probabilities using pre-race features (grid position, championship standings, circuit affinity).
* **Schema Design as Prompt Engineering:** Engineered clean analytical views (e.g., `v_mclaren_race_results`) over 15 raw tables. Self-documenting column names allow the LLM to generate highly accurate SQL without hallucinating schemas.
* **Tool Isolation Architecture:** Implemented the `BuiltInCodeExecutor` inside an isolated sub-agent (the Visualization Agent). This securely generates data visualizations in Python without causing tool-call conflicts with the BigQuery SQL executor.
* **Managed Cloud Deployment:** Packaged and deployed the ADK agent to Google Cloud's **Agent Runtime** for persistent API access, automatic scaling, and complete trace observability.

---

## 📁 Repository Structure

| Directory / File | Description |
| :--- | :--- |
| `/agent` | Contains the Python source code for the ADK root orchestrator and the visualization sub-agent. |
| `/sql` | BigQuery definitions, including BQML logistic regression models and the analytical views used to structure the F1 data. |
| `requirements.txt` | Python dependencies for the ADK, BigQuery clients, and Agent Runtime deployment. |

---

## 🚀 Getting Started

### Prerequisites
* A Google Cloud Project with billing enabled.
* Google Cloud SDK (`gcloud`) installed and configured.
* Python 3.10+

### Local Setup & Testing

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/f1-agentic-analytics.git](https://github.com/yourusername/f1-agentic-analytics.git)
   cd f1-agentic-analytics/agent
