from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///./todo_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}
)
# initialize db sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# base class, create our db model, interact with it
Base = declarative_base()

class DBContext:
    def __init__(self):
        self.db = SessionLocal()
        self.info={"FDFDFDDDDDDDDDDDDDDDDD"}

    def __enter__(self):
        return self.db

    def __exit__(self, et, ev, traceback):
        self.db.close()