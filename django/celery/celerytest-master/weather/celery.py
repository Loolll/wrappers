from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set default settings to celery from django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(['main.tasks'])

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'main.tasks.get_weather',
        'schedule': crontab(),
    },
}

