# 🚀 JobRunner

A lightweight CLI-based workflow orchestration engine built in Python, inspired by tools like Temporal and Airflow.

## 📌 Overview

JobRunner allows you to define workflows (pipelines) using YAML and execute them step-by-step with retry mechanisms, logging, and job tracking.

It is designed for:

* Automating repetitive tasks
* Running dependent shell commands
* Managing workflows locally
* Learning orchestration concepts

---

## ⚙️ Features

* ✅ YAML-based pipeline definitions
* ✅ Step-by-step execution
* ✅ Retry mechanism for failed steps
* ✅ SQLite-based job tracking
* ✅ CLI interface using Typer
* ✅ Rich terminal UI (tables, logs)
* ✅ Per-step logging system

---

## 🧱 Architecture

JobRunner follows a layered architecture similar to Spring Boot:

* **CLI Layer** → Handles user commands
* **Service Layer** → Business logic
* **Repository Layer** → Database operations
* **Engine Layer** → Executes steps
* **Parser Layer** → Reads YAML pipelines

---

## 📂 Project Structure

```
jobrunner/
├── cli/              # CLI commands
├── services/         # Business logic
├── repositories/     # DB operations
├── engine/           # Execution engine
├── parser/           # YAML parser
├── core/             # Config
├── models/           # Data models
└── utils/            # Helpers
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

## 🚀 Usage

### 1. Initialize project

```bash
python main.py init
```

### 2. Run pipeline

```bash
python main.py run pipelines/basic_success.yaml
```

### 3. Check status

```bash
python main.py status <job_id>
```

### 4. List jobs

```bash
python main.py list
```

### 5. View logs

```bash
python main.py logs <job_id>
```

### 6. Retry failed steps

```bash
python main.py retry <job_id>
```

---

## 📊 How It Works

1. YAML pipeline is parsed
2. Job + steps are stored in SQLite
3. Execution engine runs each step
4. Logs are stored per step
5. Failures trigger retries
6. Final status is recorded

---

## 🧠 Use Cases

* DevOps automation
* Batch job execution
* Task orchestration
* Learning distributed systems basics

---

## 🔮 Future Enhancements

* REST API (FastAPI integration)
* Parallel step execution
* DAG-based workflows
* UI dashboard
* Distributed workers

---

## 🛠 Tech Stack

* Python
* Typer (CLI)
* SQLite
* YAML
* Rich (CLI UI)

---

## 👨‍💻 Author

Mohammed Junaid Shaik - Intern Python Full Stack @GridDyanmics
