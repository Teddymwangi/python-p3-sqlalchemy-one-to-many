# seed/seed.py

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Game, Review

fake = Faker()

engine = create_engine('sqlite:///../one_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()

# Generate fake data and populate the database
for _ in range(10):
    game = Game(
        title=fake.name(),
        genre=fake.random_element(elements=("Action", "Adventure", "Puzzle", "RPG")),
        platform=fake.random_element(elements=("PC", "Xbox", "PlayStation", "Nintendo Switch")),
        price=fake.random_int(min=10, max=60)
    )
    session.add(game)
    session.commit()

    review = Review(
        score=fake.random_int(min=1, max=10),
        comment=fake.text(),
        game_id=game.id
    )
    session.add(review)
    session.commit()
