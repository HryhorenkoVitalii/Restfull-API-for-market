# create celery file for make

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('Restfull_API_market')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.schedule_beat = {
    'every-day': {
        "task": "tasks.discount",
        "schedule": crontab(minute=0, hour=0)
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
