# from new import User
# from new import PlaceService
# from new import Event
# from new import UserFriendlyPlace
from utils import get_number

import requests

import crud
import re
from typing import Optional
from crud import add_place

from datetime import datetime
#
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///my.db_2')
#
# Session = sessionmaker(bind=engine)
# session = Session()
cities_dictionary = {
    "ekb": "Екатеринбург",
    "kzn": "Казань",
    "msk": "Москва",
    "nnv": "Нижний Новгород",
    "nsk": "Новосибирск",
    "spb": "Санкт-Петербург"
}

response = requests.get('https://kudago.com/public-api/v1.4/places/?page=2&page_size=100') #надо собрать со всех страниц - пока 100 по умолчанию взято
data = response.json()
print(data)
places_lst = []

for every_place in data["results"]:
    city_code = every_place.get("location")


    crud.add_place(name=every_place.get("title"), description=None, country= None, district=None, street=None, num_building =None, liter_building=None, level=None, city=cities_dictionary.get(city_code), mono_address=every_place.get("address"), phone=get_number(every_place.get('phone')))



# class PlaceService:
#     def __init__ (self, data):
#
#         self.name = data.get("title")
#         self.description = None
#         self.country =  None
#         self.city_code = data.get("location")
#         self.city = cities_dictionary.get(self.city_code)
#         self.district = None
#         self.street =  None
#
#
#         self.num_building =  None
#         self.liter_building =  None
#         self.level =  None
#         self.mono_address = data.get("location")
#
#
# print(places_lst)
#
# for p in places_lst:
#     print(p.__dict__.values())



#     session.add(p)
# session.commit()
