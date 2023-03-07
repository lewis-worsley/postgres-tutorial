from sqlalchemy import (
    create_engine, Column, Integer, String, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "countries" table
class Countries(base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    population = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

costa_rica = Countries(
    country = "Costa Rica",
    city = "San Jose",
    population = 5.1
)

spain = Countries(
    country = "Spain",
    city = "Madrid",
    population = 47.4
)

# add each instance of our programmers to our session
# session.add(costa_rica)
# session.add(spain)

# commit our session to the database
# session.commit()

# query the database to find all countries
all_countries = session.query(Countries)
for countries in all_countries:
    print(
        countries.id,
        countries.country,
        countries.city,
        countries.population,
        sep=" | "
    )