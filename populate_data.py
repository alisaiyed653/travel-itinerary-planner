from app.db import SessionLocal
from app.models import Destination, Attraction



db = SessionLocal()

data = {
    "Paris": [
        {"name": "Eiffel Tower", "description": "Paris's most iconic landmark, offering panoramic views of the city from its various viewing platforms. A symbol of French ingenuity and a must-visit for its breathtaking vistas.", "image_url": "/static/images/eiffel_tower.jpg"},
        {"name": "Louvre Museum", "description": "The world's largest art museum and a historic monument in Paris. It's home to thousands of works, including the Mona Lisa and the Venus de Milo.", "image_url": "/static/images/louvre.jpg"},
        {"name": "Notre Dame Cathedral", "description": "A masterpiece of French Gothic architecture, famous for its intricate facades, stained glass, and the dramatic tale of Quasimodo, the Hunchback of Notre-Dame.", "image_url": "/static/images/notre.jpg"},
        
    ],
    "New York": [
        {"name": "Statue of Liberty", "description": "A monumental gift from France, this iconic statue on Liberty Island symbolizes freedom and democracy.", "image_url": "/static/images/statueofliberty.jpg"},
        {"name": "Central Park", "description": "A sprawling urban oasis in Manhattan offering a mix of natural scenery, recreational facilities, and cultural attractions.", "image_url": "/static/images/central_park.jpg"},
        {"name": "Metropolitan Museum of Art (The Met)", "description": "One of the largest art museums in the world, showcasing an extensive collection that spans 5,000 years of global culture.", "image_url": "/static/images/met.jpg"},
    ],
    "Doha": [
        {"name": "Tokyo Tower", "description": "Landmark observation tower.", "image_url": "https://example.com/tokyo_tower.jpg"},
        {"name": "Senso-ji Temple", "description": "Historic Buddhist temple.", "image_url": "https://example.com/senso_ji.jpg"},
        
    ],
    "London": [
        {"name": "Big Ben", "description": "Famous clock tower.", "image_url": "https://example.com/big_ben.jpg"},
        {"name": "Tower of London", "description": "Historic castle and prison.", "image_url": "https://example.com/tower_london.jpg"},
        
    ],
    "Dubai": [
        {"name": "Burj Khalifa", "description": "Tallest building in the world.", "image_url": "https://example.com/burj_khalifa.jpg"},
        {"name": "Dubai Mall", "description": "One of the largest shopping malls.", "image_url": "https://example.com/dubai_mall.jpg"},
        
    ],
}

# Populate database
for destination_name, attractions in data.items():
    # Add destination
    destination = Destination(name=destination_name)
    db.add(destination)
    db.commit()
    db.refresh(destination)
    
    # Add attractions for this destination
    for attraction in attractions:
        db.add(Attraction(
            destination_id=destination.id,
            name=attraction["name"],
            description=attraction["description"],
            image_url=attraction["image_url"]
        ))
    db.commit()

db.close()
