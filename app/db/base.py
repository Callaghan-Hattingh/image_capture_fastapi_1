import os
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()

sqlite_url = f"sqlite:///{os.getenv('SQLITE_DB_NAME')}.db"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=False, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
