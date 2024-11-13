# Travel Itinerary Planner

This is a **Travel Itinerary Planner** project with three primary components:
- **UI**: A simple frontend interface built with HTML, CSS, and JavaScript for inputting travel destinations and duration.
- **API**: A backend API created with FastAPI, handling requests and generating itineraries.
- **Database**: Persistent storage for data, which will be connected to the API to save and retrieve itinerary information.

---

## Features
- **User-friendly interface** to interact with the API.
- **Backend API** endpoints for generating and managing itineraries.
- **Modular design** with separate components for UI, API, and database.

---

## Setup and Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html) or another database for local storage

### Steps

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/travel-itinerary-planner.git
   cd travel-itinerary-planner
   ```

2. **Set up Virtual enviroment**:
```
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
```
3. **Run FastAPI app**:
```
    uvicorn app.main:app --reload
```
## Project Struture

travel_itinerary_planner/
├── app/                      # Backend API
│   ├── main.py               # FastAPI main file
│   ├── crud/                 # CRUD operations for the API
│   ├── db/                   # Database connection scripts
│   ├── itinerary/            # Core itinerary logic
│   ├── models/               # Database models
│   ├── schemas/              # Pydantic data validation schemas
│   ├── static/               # Static files for UI
│   │   ├── css/              # CSS files
│   │   ├── images/           # Images for the UI
│   │   └── js/               # JavaScript files
│   └── templates/            # HTML templates
│       ├── index.html        # Main HTML file
│       └── itinerary.html    # Itinerary display HTML file
├── populate_data.py          # Script to populate database with sample data
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── travel_itinerary.db       # SQLite database file


## Future Enhancements

This app was designed and built in this way for me to demonstrate my DevOps skills. This microservices-style setup allows you to create separate containers for the UI, API, and database, making your architecture more modular, scalable, and maintainable.

- Dockerize each component to run in separate containers.
- CI/CD Pipeline setup using Jenkins for continuous integration and deployment for each component
- Kubernetes deployment on AWS EKS for scalability.