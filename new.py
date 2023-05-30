from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from sqlalchemy.orm import relationship as rs

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(30))
    l_name = Column(String(30))
    nickname = Column(String(30), unique=True, nullable=True)
    birthday = Column(Integer)
    now_place = Column(Integer, ForeignKey('place.id'))
    phone = Column(Integer)
    e_mail = Column(String(50), unique=True, nullable=True)


class Event(db.Model):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=True)
    description = Column(String(3000))
    art_form = Column(Integer, ForeignKey('art_form.id'))
    genre = Column(Integer, ForeignKey('genre.id'))
    date_time = Column(Integer)
    dt_start = Column(Integer)
    dt_over = Column(Integer)
    cost_min = Column(Integer)
    cost_max = Column(Integer)
    currency = Column(String(3))
    organizer = Column(Integer, ForeignKey('organizer.id'))
    place = Column(Integer, ForeignKey('place.id'))
    link = Column(String(1000), unique=True, nullable=True)
    photo = Column(String(2000))


class Organizer(db.Model):
    __tablename__ = 'organizer'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), unique=True, nullable=True)
    description = Column(String(3000))


class Place(db.Model):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True)
    name = Column(String(3000),  nullable=True)
    description = Column(String(3000))
    country = Column(String(30), default='Россия')
    city = Column(String(50))
    district = Column(String(100))
    street = Column(String(100))
    num_building = Column(Integer)
    liter_building = Column(String(5))
    level = Column(Integer)
    mono_address = Column(String(200))
    phone = Column(String(20))


class Genre(db.Model):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class ArtForm(db.Model):
    __tablename__ = 'art_form'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class UserFriendlyEvent(db.Model):
    __tablename__ = 'user_friendly_event'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_event = Column(Integer, ForeignKey('event.id'))
    friendly = Column(Boolean)
    is_visit = Column(Boolean)


class UserFriendlyGenre(db.Model):
    __tablename__ = 'user_friendly_genre'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_genre = Column(Integer, ForeignKey('genre.id'))
    friendly = Column(Boolean)


class UserFriendlyArtForm(db.Model):
    __tablename__ = 'user_friendly_artform'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_artform = Column(Integer, ForeignKey('art_form.id'))
    friendly = Column(Boolean)


class UserFriendlyOrganizer(db.Model):
    __tablename__ = 'user_friendly_organizer'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_organizer = Column(Integer, ForeignKey('organizer.id'))
    friendly = Column(Boolean)


class UserFriendlyPlace(db.Model):
    __tablename__ = 'user_friendly_place'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_place = Column(Integer, ForeignKey('place.id'))
    friendly = Column(Boolean)


with app.app_context():
    db.create_all()
