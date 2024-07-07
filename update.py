from sqlalchemy import create_engine, Column, Integer, String, update
from setup import session_restaurants, Restaurant, session_hotels, Hotel

# Update one of the restaurant records
restaurant_to_update = session_restaurants.query(Restaurant) \
    .filter(Restaurant.restaurant_name == "NYC Diner") \
    .one()

# Update the famous_dish column
restaurant_to_update.famous_dish = "Pancakes and Maple Syrup"
# You can update any other column if needed
# e.g., restaurant_to_update.restaurant_address = "New Address"

# Commit the changes
session_restaurants.commit()

# Update one of the hotel records
hotel_to_update = session_hotels.query(Hotel) \
    .filter(Hotel.hotel_name == "Hilton NYC") \
    .one()

# Update the hotel_city column
hotel_to_update.hotel_city = "Los Angeles"
# You can update any other column if needed
# e.g., hotel_to_update.number_of_rooms = 150

# Commit the changes
session_hotels.commit()

