from jobrunner.repositories.job_repository import *
from jobrunner.engine.runner import run_job

def init_project():
    from jobrunner.core.config import BASE_DIR, LOG_DIR, DB_PATH

    BASE_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)
    DB_PATH.touch(exist_ok=True)

    create_tables()


def run_pipeline(pipeline):
    job_id = create_job(pipeline["name"])
    create_steps(job_id, pipeline["steps"])
    run_job(job_id)
    return job_id