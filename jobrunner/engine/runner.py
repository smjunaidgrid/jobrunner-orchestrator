import subprocess
from pathlib import Path
from jobrunner.db.connection import get_connection
from jobrunner.core.config import LOG_DIR

def run_job(job_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, command, retry_count, max_retries FROM steps WHERE job_id=? ORDER BY rowid",
        (job_id,),
    )

    steps = cursor.fetchall()

    for step_id, name, command, retry_count, max_retries in steps:
        attempt = retry_count

        while attempt <= max_retries:
            cursor.execute(
                "UPDATE steps SET status='running', started_at=datetime('now') WHERE id=?",
                (step_id,),
            )
            conn.commit()

            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            log_dir = LOG_DIR / job_id
            log_dir.mkdir(parents=True, exist_ok=True)

            with open(log_dir / f"{name}_{attempt}.log", "w") as f:
                f.write(result.stdout + result.stderr)

            if result.returncode == 0:
                cursor.execute(
                    "UPDATE steps SET status='success', completed_at=datetime('now'), retry_count=? WHERE id=?",
                    (attempt, step_id),
                )
                conn.commit()
                break

            attempt += 1
            cursor.execute("UPDATE steps SET retry_count=? WHERE id=?", (attempt, step_id))
            conn.commit()

            if attempt > max_retries:
                cursor.execute("UPDATE steps SET status='failed' WHERE id=?", (step_id,))
                cursor.execute("UPDATE jobs SET status='failed' WHERE id=?", (job_id,))
                conn.commit()
                conn.close()
                return

    cursor.execute("UPDATE jobs SET status='success' WHERE id=?", (job_id,))
    conn.commit()
    conn.close()