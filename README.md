# Local LLM SQL Evaluation Framework

A fully automated evaluation framework for benchmarking local Large Language Models (LLMs) on SQL generation tasks using Ollama and SQLite.

This project evaluates the SQL proficiency of locally running coding-focused LLMs by generating SQL queries from natural language questions, executing them against a database, and computing evaluation metrics such as execution accuracy, valid SQL rate, exact match accuracy, and latency.

---

# Features

- Automated SQL generation benchmarking
- Local LLM evaluation using Ollama
- SQLite-based query execution
- Multi-model benchmarking support
- Execution-based SQL evaluation
- Exact match evaluation
- SQL syntax validation
- Latency tracking
- CSV leaderboard generation
- Modular project architecture
- Easily extensible benchmark dataset

---

# Supported Models

The framework is designed for locally running coding-focused LLMs such as:

- Qwen2.5-Coder
- DeepSeek-Coder
- Mistral
- Phi-3
- Any Ollama-compatible local model

---

# Project Architecture

```text
sql-llm-eval/
│
├── database/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── company.db
│
├── datasets/
│   └── sql_questions.json
│
├── evaluator/
│   ├── execute_sql.py
│   ├── metrics.py
│   └── evaluator.py
│
├── models/
│   └── ollama_client.py
│
├── prompts/
│   └── sql_prompt.txt
│
├── results/
│
├── visualizations/
│
├── setup_database.py
├── test_ollama.py
├── test_sql_execution.py
├── test_dataset.py
├── main.py
└── requirements.txt
```

---

# Evaluation Workflow

```text
Natural Language Question
            ↓
      Local LLM
            ↓
    Generated SQL
            ↓
    SQLite Execution
            ↓
    Output Comparison
            ↓
    Metric Calculation
            ↓
      Leaderboard
```

---

# Evaluation Metrics

The framework evaluates models using:

- Execution Accuracy
- Valid SQL Rate
- Exact Match Accuracy
- Latency Measurement

---

# Tech Stack

| Component | Technology |
|---|---|
| Local LLM Serving | Ollama |
| Database | SQLite |
| Evaluation Engine | Python |
| Data Processing | Pandas |
| Visualization | Matplotlib |

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd sql-llm-eval
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama from:

https://ollama.com

---

## Pull Models

### Qwen2.5-Coder

```bash
ollama pull qwen2.5-coder:7b
```

### DeepSeek-Coder

```bash
ollama pull deepseek-coder:6.7b
```

### Mistral

```bash
ollama pull mistral:7b
```

---

# Database Setup

Run:

```bash
python setup_database.py
```

This creates:
- SQLite database
- tables
- sample records

---

# Running Validation Tests

## Test Ollama Connection

```bash
python test_ollama.py
```

---

## Test SQL Execution

```bash
python test_sql_execution.py
```

---

## Test Dataset Loading

```bash
python test_dataset.py
```

---

# Run Full Evaluation

```bash
python main.py
```

The framework will:
- load benchmark questions
- generate SQL using local LLMs
- execute generated queries
- compute evaluation metrics
- generate CSV outputs

---

# Dataset Format

Example dataset entry:

```json
{
    "id": 1,
    "difficulty": "easy",
    "question": "Retrieve all employee details.",
    "answer": "SELECT * FROM employees;"
}
```

---

# Extending the Project

You can extend the framework by adding:

- Spider benchmark integration
- BIRD benchmark integration
- Hallucination detection
- Query optimization scoring
- RAG-based schema retrieval
- Conversational SQL evaluation
- Visualization dashboards
- Multi-turn SQL evaluation
- Advanced semantic SQL matching

---

# Use Cases

- Local LLM benchmarking
- SQL capability evaluation
- Text-to-SQL research
- Coding model comparison
- GenAI systems experimentation
- Execution-based LLM evaluation

---

# Future Improvements

- Semantic SQL evaluation
- SQL normalization
- Robust query cleaning
- Better exact-match scoring
- Parallel model evaluation
- Advanced leaderboard analytics

---
