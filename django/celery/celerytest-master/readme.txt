Here the process of the creating shedule of some events.
We will use celery(cron)+reddis.

1) We need to install and up redis server
It's very simple and we can do it less than three minutes.
It's the many way how we can do it.
When the redis is installed, it's better to test it.

2) Install django-celery.
pip install django-celery

3) In settings define this parametres:

# Redis settings

REDIS_HOST = 'localhost'  # Redis host
REDIS_PORT = '6379'  # Redis port
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'  # Broker url
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # Broker transport options
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'  # Celery backend

# Celery settings

# CELERY_BROKER_URL = 
CELERY_ACCEPT_CONTENT = ['json']  # Content
CELERY_TASK_SERIALIZER = 'json'  # Content

4)In $project_name$ folder which contains settings file create new file celery.py.
# At first need to import all modules 

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
 
# set default settings to celery from django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(['main.tasks'])
# It's was the basic part of the celery inition. 

# Then we need to create schedules. For ex: every minute action. 
# It's provides some_task task which includes in main app

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'main.tasks.some_task',
        'schedule': crontab(),
    },
}

5) Some words about tasks. Create tasks in some_app.tasks(py)
# Here is example of tasks.py file 

from __future__ import absolute_import, unicode_literals
from $project_name$.celery import app

# task
@app.task
def some_func(*args, **kwargs):
	...

6) All in one about project init
	a)run django project
		python3 manage.py runserver
	b)run redis server
		redis-server
	c)run celery worker 
		celery worker -A $project_name$
	d)run celery schedule
		celery beat -A $project_name$

7) That's all !!!
When I made it first, I'm faced with the problem that was caused by version mismatch.
It was fixed by changing celery version on previos stable version. 