# testing/test.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Game, Review

engine = create_engine('sqlite:///../one_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()

def test_review_belongs_to_game():
    review = session.query(Review).first()
    assert review.game_id == review.game.id

def test_game_has_many_reviews():
    game = session.query(Game).first()
    assert len(game.reviews) > 0
