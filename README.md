# Enterprise F1 Racing Intelligence Platform

An AI-powered analytics platform demonstrating multi-tier agentic architecture, built on Google Cloud. This project orchestrates document retrieval, no-code agent workflows, and a code-first Agent Development Kit (ADK) to process 70+ years of Formula 1 telemetry and FIA regulations.

## Architecture Overview
This platform solves the core enterprise AI challenge: matching the right data architecture to the right query type. 

1. **Retrieval Layer (RAG):** Grounded in official 2025/2026 FIA regulatory PDFs to provide cited, hallucination-free rule interpretations.
2. **Orchestration Layer:** A multi-agent system synthesizing proprietary driver profiles, live web data, and regulations for comprehensive race briefings.
3. **Computation Layer (ADK):** A code-first Python agent with direct BigQuery access to run live SQL, execute BQML podium predictions, and generate isolated Python visualizations.

## Key Technical Highlights
* **BigQuery ML (BQML):** Trained a logistic regression model entirely in SQL to predict podium probabilities using pre-race features.
* **Tool Isolation:** Implemented the `BuiltInCodeExecutor` in an isolated sub-agent to securely generate data visualizations without tool conflicts.
* **Agent Runtime Deployment:** Packaged and deployed the ADK agent to managed cloud infrastructure for persistent API access and trace observability.