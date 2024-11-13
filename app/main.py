from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import app.crud as crud
import os

# Debug statement to print all attributes in the crud module
print("Available attributes in crud:", dir(crud))

from . import models, itinerary
from .db import SessionLocal, engine

app = FastAPI()

# Mount static files to serve CSS and JavaScript
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")



# Set up the templates directory for rendering HTML files
templates_path = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_path)
print("Templates directory path:", templates_path)  # Debug path to ensure correctness

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Serve index.html at the root URL
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Serialize the attraction to make it JSON serializable
def serialize_attraction(attraction):
    return {
        "id": attraction.id,
        "name": attraction.name,
        "description": attraction.description,
        "image_url": attraction.image_url,
        "destination_id": attraction.destination_id
    }

@app.get("/generate_itinerary/")
def generate_itinerary(destination: str, days: int, db: Session = Depends(get_db)):
    print(f"Request received for destination: {destination}, days: {days}")
    attractions = crud.fetch_attractions_by_destination(db, destination)
    print("Fetched attractions:", attractions)

    # Generate itinerary and serialize the objects
    itinerary_plan = itinerary.generate_itinerary(attractions, days)
    serialized_itinerary = {day: [serialize_attraction(attr) for attr in attrs] for day, attrs in itinerary_plan.items()}
    print("Generated serialized itinerary:", serialized_itinerary)

    return serialized_itinerary

# Serve itinerary.html for displaying the itinerary
@app.get("/itinerary.html", response_class=HTMLResponse)  # Update route to match JavaScript reference
async def show_itinerary_page(request: Request):
    return templates.TemplateResponse("itinerary.html", {"request": request})

