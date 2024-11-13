from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Destination(Base):
    __tablename__ = "destinations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # Relationship to the Attraction model
    attractions = relationship("Attraction", back_populates="destination", cascade="all, delete-orphan")

class Attraction(Base):
    __tablename__ = "attractions"
    id = Column(Integer, primary_key=True, index=True)
    # Foreign key to reference the Destination table
    destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"))
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    # Relationship to the Destination model
    destination = relationship("Destination", back_populates="attractions")

