import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project16012024.settings')

app = Celery('News')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()
app.conf.beat_schedule = {
   'send_mail_monday_8am': {
         'task': 'main_app.tasks.send_mail_monday_8am',
       'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
     },
 }

