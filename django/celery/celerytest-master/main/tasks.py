# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from weather.celery import app
from main.models import Weather
from datetime import datetime


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@app.task
def prnt(string: str):
    return string


@app.task
def get_weather():
    print('ok')
    Weather.objects.create(digit=str(datetime.now())[-1])

@app.task
def func():
    with open('file.txt', 'a') as file:
        file.write('1')
