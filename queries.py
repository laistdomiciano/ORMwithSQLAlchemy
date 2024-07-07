# from setup import session_restaurants, Restaurant
#
# restaurants = session_restaurants.query(Restaurant).all()
#
# for restaurant in restaurants:
#     print(restaurant.restaurant_name, restaurant.restaurant_city)
#
# restaurants = session_restaurants.query(Restaurant) \
#     .order_by(Restaurant.restaurant_name.asc()) \
#     .all()
#
# for restaurant in restaurants:
#     print(restaurant.restaurant_name, restaurant.restaurant_city)
#
# restaurant = session_restaurants.query(Restaurant) \
#     .filter(Restaurant.restaurant_name == 'NYC Diner') \
#     .one()
#
# print(restaurant)

from setup import session_restaurants, Restaurant
from sqlalchemy import or_

restaurants = session_restaurants.query(Restaurant) \
    .filter(or_(Restaurant.restaurant_city == 'London', Restaurant.restaurant_city == 'Las Vegas')) \
    .all()

for restaurant in restaurants:
    print(restaurant.restaurant_name, restaurant.restaurant_city)
