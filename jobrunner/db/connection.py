import sqlite3
from jobrunner.core.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)
