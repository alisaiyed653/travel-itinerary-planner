# itinerary.py

def generate_itinerary(attractions, days):
    """
    Generates an itinerary by dividing attractions over the specified days.

    :param attractions: List of attractions for a destination
    :param days: Number of days for the itinerary
    :return: Dictionary with day-wise itinerary
    """
    itinerary_plan = {}
    attractions_per_day = max(1, len(attractions) // days)  # Distribute attractions evenly

    for day in range(1, days + 1):
        start_index = (day - 1) * attractions_per_day
        end_index = start_index + attractions_per_day
        itinerary_plan[day] = attractions[start_index:end_index]

    return itinerary_plan
