"""Дата-файл для тестирования RestFul API, auth"""
# -*- coding: utf-8 -*-
from model.get_booking_model import RequestCreateModel

request = RequestCreateModel(firstname="Sara", lastname="Konor",
                             totalprice=400, depositpaid=True,
                             bookingdates={"checkin": "2114-11-12",
                                           "checkout": "2114-12-12"},
                             additionalneeds="Breakfast")

data = [request]
