import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


DB_TYPE = os.getenv("DB_TYPE", "sqlite")

if DB_TYPE == "sqlite":
    DATABASE_URL = "sqlite:///production_planner.db"

elif DB_TYPE == "postgresql":
    DATABASE_URL = (
        f"postgresql+psycopg://"
        f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
        f"/{os.getenv('DB_NAME')}"
    )

else:
    raise ValueError("DB_TYPE must be 'sqlite' or 'postgresql'")

engine = create_engine(DATABASE_URL)