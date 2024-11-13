from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Ensure models is imported here

SQLALCHEMY_DATABASE_URL = "sqlite:///./travel_itinerary.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database
Base.metadata.create_all(bind=engine)

