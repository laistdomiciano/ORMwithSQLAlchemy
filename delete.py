from setup import session_restaurants, Restaurant

# Delete a specific restaurant by its ID
session_restaurants.query(Restaurant) \
    .filter(Restaurant.restaurant_id == 3) \
    .delete()

# Commit the changes
session_restaurants.commit()

# Specify the city you want to remove all restaurants from
city_to_remove = "Los Angeles"  # Replace with the actual city name

# Delete all restaurants in the specified city
session_restaurants.query(Restaurant) \
    .filter(Restaurant.restaurant_city == city_to_remove) \
    .delete()

# Commit the changes
session_restaurants.commit()