import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the path to the database files
db_path_restaurants = 'data/restaurants.sqlite'
db_path_hotels = 'data/hotels.sqlite'
db_dir = os.path.dirname(db_path_restaurants)

# Ensure the directory exists
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Create separate database connections
engine_restaurants = create_engine(f'sqlite:///{db_path_restaurants}')
engine_hotels = create_engine(f'sqlite:///{db_path_hotels}')

# Create separate database sessions
SessionRestaurants = sessionmaker(bind=engine_restaurants)
SessionHotels = sessionmaker(bind=engine_hotels)

session_restaurants = SessionRestaurants()
session_hotels = SessionHotels()

# Define the data table class's parent class
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column(String)
    restaurant_city = Column(String)
    famous_dish = Column(String)

    def __repr__(self):
        return f"Restaurant(restaurant_id={self.restaurant_id}, name={self.restaurant_name})"

class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String)
    hotel_city = Column(String)

    def __repr__(self):
        return f"Hotel(hotel_id={self.hotel_id}, name={self.hotel_name})"

# Create tables in the respective databases
Base.metadata.create_all(engine_restaurants, tables=[Restaurant.__table__])
Base.metadata.create_all(engine_hotels, tables=[Hotel.__table__])

# Create an instance of the Restaurant table class
restaurant = Restaurant(
    restaurant_name="NYC Diner",
    restaurant_city="New York City",
    famous_dish="Eggs Benedict"
)

# Since the session is already open, add the new restaurant record
session_restaurants.add(restaurant)
session_restaurants.commit()

# Verify the restaurant record was added
restaurant_record = session_restaurants.query(Restaurant).first()
print(f"Added Restaurant: {restaurant_record}")

# Create an instance of the Hotel table class
hotel = Hotel(
    hotel_name="Grand Plaza",
    hotel_city="New York City"
)

# Since the session is already open, add the new hotel record
session_hotels.add(hotel)
session_hotels.commit()

# Verify the hotel record was added
hotel_record = session_hotels.query(Hotel).first()
print(f"Added Hotel: {hotel_record}")
