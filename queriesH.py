from setup import session_hotels, Hotel
from sqlalchemy import desc

# 1. Retrieve all hotels in reverse alphabetical order.
hotels_reverse_alphabetical = session_hotels.query(Hotel) \
    .order_by(desc(Hotel.hotel_name)) \
    .all()

print("Hotels in reverse alphabetical order:")
for hotel in hotels_reverse_alphabetical:
    print(hotel.hotel_name, hotel.hotel_city)

# 2. Retrieve all hotels in a specific city.
specific_city = 'New York'  # replace with the city you want to filter by
hotels_in_city = session_hotels.query(Hotel) \
    .filter(Hotel.hotel_city == specific_city) \
    .all()

print(f"\nHotels in {specific_city}:")
for hotel in hotels_in_city:
    print(hotel.hotel_name, hotel.hotel_city)

# 3. Retrieve all hotels whose names begin with a specific letter.
specific_letter = 'H'  # replace with the letter you want to filter by
hotels_with_letter = session_hotels.query(Hotel) \
    .filter(Hotel.hotel_name.like(f'{specific_letter}%')) \
    .all()

print(f"\nHotels starting with '{specific_letter}':")
for hotel in hotels_with_letter:
    print(hotel.hotel_name, hotel.hotel_city)
