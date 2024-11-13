document.addEventListener('DOMContentLoaded', function () {
    console.log("scripts.js loaded"); // Check if the script loads

    // JavaScript for index.html
    const itineraryForm = document.getElementById('itinerary-form');
    if (itineraryForm) {
        console.log("Form found on index.html");
        itineraryForm.addEventListener('submit', async function (event) {
            event.preventDefault(); // Prevents default form submission
            console.log("Form submission prevented");

            // Get user input values
            const destination = document.getElementById('destination').value;
            const days = document.getElementById('days').value;
            console.log(`Destination: ${destination}, Days: ${days}`);

            try {
                // Fetch itinerary data from the backend API
                const response = await fetch(`/generate_itinerary/?destination=${destination}&days=${days}`);
                const itinerary = await response.json();

                console.log("Fetched itinerary:", itinerary);

                // Store itinerary data in localStorage to access in itinerary.html
                localStorage.setItem("itinerary", JSON.stringify(itinerary));

                // Redirect to the itinerary.html page
                window.location.href = "/itinerary.html";
            } catch (error) {
                console.error("Error fetching itinerary:", error);
                alert("Could not generate itinerary. Please try again.");
            }
        });
    } else {
        console.log("No form found; assuming this is itinerary.html");
    }

    // JavaScript for itinerary.html
    const itineraryDiv = document.getElementById("itinerary");
    if (itineraryDiv) {
        console.log("Displaying itinerary on itinerary.html");

        // Retrieve itinerary data from localStorage
        const itineraryData = JSON.parse(localStorage.getItem("itinerary"));
        
        if (itineraryData) {
            itineraryDiv.innerHTML = "<h2>Itinerary:</h2>";
            Object.keys(itineraryData).forEach(day => {
                const dayDiv = document.createElement('div');
                dayDiv.innerHTML = `<h3>Day ${day}</h3>`;

                itineraryData[day].forEach(attraction => {
                    const attractionDiv = document.createElement('div');
                    attractionDiv.innerHTML = `
                        <strong>${attraction.name}</strong><br>
                        <img src="${attraction.image_url}" alt="${attraction.name}" style="width: 150px; height: auto;"><br>
                        ${attraction.description}
                    `;
                    dayDiv.appendChild(attractionDiv);
                });

                itineraryDiv.appendChild(dayDiv);
            });
        } else {
            itineraryDiv.innerHTML = "<p>No itinerary data found. Please go back and generate an itinerary.</p>";
        }
    }
});

