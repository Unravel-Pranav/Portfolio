from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.config.config import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()
