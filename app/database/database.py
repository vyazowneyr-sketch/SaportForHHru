from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(str(settings.DATABASE_URL))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()