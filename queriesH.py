from setup import session_hotels, Hotel

hotels = session_hotels.query(Hotel) \
    .order_by(Hotel.hotel_name.asc()) \
    .all()

for hotel in hotels:
    print(hotel.hotel_name, hotel.hotel_city)