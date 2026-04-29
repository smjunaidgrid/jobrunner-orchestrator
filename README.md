# 🚀 JobRunner

A lightweight, extensible **workflow orchestration engine** built in Python, designed to execute YAML-defined pipelines with reliability, observability, and modular architecture.

Inspired by systems like **Temporal** and **Apache Airflow**, JobRunner provides a simplified yet powerful foundation for task orchestration and automation.

---

## 📌 Overview

JobRunner enables developers to define and execute workflows using declarative YAML configurations. Each workflow (pipeline) consists of ordered steps that are executed sequentially with built-in support for retries, logging, and state tracking.

The system is designed to be:

* Simple to use (CLI-driven)
* Modular and extensible
* Suitable for learning orchestration concepts
* Scalable into production-grade systems

---

## ⚙️ Key Features

* **YAML-based Workflow Definitions**
  Define pipelines declaratively with step-wise commands.

* **Deterministic Execution Engine**
  Executes steps sequentially with clear state transitions.

* **Retry Mechanism**
  Automatically retries failed steps based on configuration.

* **Persistent Job Tracking (SQLite)**
  Tracks job and step states with timestamps.

* **Structured Logging System**
  Stores logs per job and per step for debugging and auditing.

* **CLI Interface (Typer + Rich)**
  Provides an interactive and readable terminal experience.

---

## 🧱 Architecture

JobRunner follows a **layered architecture**, inspired by enterprise backend systems (e.g., Spring Boot):

| Layer                | Responsibility                                 |
| -------------------- | ---------------------------------------------- |
| **CLI Layer**        | Handles user interaction and command execution |
| **Service Layer**    | Encapsulates business logic                    |
| **Repository Layer** | Manages database operations                    |
| **Engine Layer**     | Executes pipeline steps                        |
| **Parser Layer**     | Parses and validates YAML pipelines            |
| **Core Layer**       | Centralized configuration                      |

---

## 📂 Project Structure

```
project01/
│
├── jobrunner/
│   ├── cli/              # CLI commands (controllers)
│   ├── services/         # Business logic
│   ├── repositories/     # Database access layer
│   ├── engine/           # Execution engine
│   ├── parser/           # YAML parser
│   ├── core/             # Configuration
│   ├── db/               # DB connection handling
│   └── utils/            # Utilities
│
├── pipelines/            # YAML workflow definitions
├── .jobrunner/           # Runtime data (DB + logs)
├── main.py
└── requirements.txt
```

---

## 🧪 Sample Pipeline

```yaml
name: basic_success

steps:
  - name: hello
    command: "echo Hello World"
    retry: 0

  - name: done
    command: "echo Completed"
    retry: 1
```

---

## 🚀 Getting Started

### 1. Initialize the Environment

```bash
python main.py init
```

Creates:

* `.jobrunner/jobs.db` (SQLite database)
* `.jobrunner/logs/` (execution logs)

---

### 2. Run a Pipeline

```bash
python main.py run pipelines/basic_success.yaml
```

---

### 3. Check Job Status

```bash
python main.py status <job_id>
```

Displays:

* Step execution status
* Retry counts
* Timestamps

---

### 4. List All Jobs

```bash
python main.py list
```

---

### 5. View Logs

```bash
python main.py logs <job_id>
```

---

### 6. Retry Failed Jobs

```bash
python main.py retry <job_id>
```

---

## 📊 Execution Flow

1. Pipeline YAML is parsed and validated
2. Job and steps are persisted in SQLite
3. Execution engine processes each step sequentially
4. Logs are generated per step
5. Failures trigger retries based on configuration
6. Final job status is updated

---

## 🧠 Use Cases

* CLI-based DevOps automation
* Batch job execution pipelines
* Local workflow orchestration
* Learning distributed systems and schedulers
* Prototyping orchestration engines

---

## 🔍 Design Highlights

* **Separation of Concerns**: Clear distinction between layers
* **Extensibility**: Easy to plug in APIs, async workers, or message queues
* **Observability**: Logs + DB tracking provide traceability
* **Fault Tolerance**: Built-in retry mechanism

---

## 🔮 Future Enhancements

* REST API layer (FastAPI)
* Parallel and asynchronous execution
* DAG-based workflow support
* Web-based dashboard (UI)
* Distributed worker architecture (queue-based)
* Integration with Docker/Kubernetes

---

## 🛠 Tech Stack

* **Python**
* **Typer** (CLI framework)
* **Rich** (terminal UI)
* **SQLite** (lightweight persistence)
* **PyYAML** (pipeline parsing)

---

## 👨‍💻 Author

**Mohammed Junaid Shaik**
Python Full Stack Intern @ Grid Dynamics

---

## 📎 Note

This project started as a CLI-based workflow engine and was later **refactored into a modular, production-style architecture**, aligning with backend engineering best practices.

It serves as a strong foundation for building **scalable orchestration systems**.
