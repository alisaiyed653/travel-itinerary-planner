from sqlalchemy.orm import Session
from .models import Destination, Attraction

def fetch_attractions_by_destination(db: Session, destination_name: str):
    # Find the destination by name
    destination = db.query(Destination).filter(Destination.name == destination_name).first()
    
    # Return attractions if the destination exists
    if destination:
        return db.query(Attraction).filter(Attraction.destination_id == destination.id).all()
    else:
        return []

