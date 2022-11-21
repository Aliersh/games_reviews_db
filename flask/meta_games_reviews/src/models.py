from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Developers(db.Model):
    __tablename__ = 'developers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Publishers(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    genre = db.Column(db.String, nullable=False)
    esrb_rating = db.Column(db.String)
    release_date = db.Column(db.Date, nullable=False)
    multiplayer = db.Column(db.Boolean)
    developer_id =  db.Column(db.Integer, db.ForeignKey('developers.id'), nullable=False)
    publisher_id =  db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)

    def __init__(self, name: str, genre: str, esrb_rating: str, release_date: datetime, multiplayer: bool, developer_id: int, publisher_id: int):
        self.name = name
        self.genre = genre
        self.esrb_rating = esrb_rating
        self.release_date = release_date
        self.multiplayer = multiplayer
        self.developer_id = developer_id
        self.publisher_id = publisher_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'esrb_rating': self.esrb_rating,
            'release_date': self.release_date.isoformat(),
            'multiplayer': self.multiplayer,
            'developer_id': self.developer_id,
            'publisher_id': self.publisher_id
        }

class Platforms(db.Model):
    __tablename__ = 'platforms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Review_sites(db.Model):
    __tablename__ = 'review_sites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Bridge tables

games_reviews = db.Table(
    'games_reviews',
    db.Column(
        'score', db.Integer,
        nullable=False
    ),

    db.Column(
        'total_reviews', db.Integer,
        nullable=False
    ),

    db.Column(
        'recommendation', db.Float,
        nullable=True
    ),

    db.Column(
        'positive_reviews', db.Integer,
        nullable=True
    ),

    db.Column(
        'game_id', db.Integer,
        db.ForeignKey('games.id'),
        primary_key=True
    ),

    db.Column(
        'review_site_id', db.Integer,
        db.ForeignKey('review_sites.id'),
        primary_key=True
    )
)

games_platforms = db.Table(
    'games_platforms',
    db.Column(
        'game_id', db.Integer,
        db.ForeignKey('games.id'),
        primary_key=True
    ),

    db.Column(
        'platform_id', db.Integer,
        db.ForeignKey('platforms.id'),
        primary_key=True
    )
)