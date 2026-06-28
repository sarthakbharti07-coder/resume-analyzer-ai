from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "check_hostname": False,
            "verify_mode": 0,
        }
    },
)

sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()
