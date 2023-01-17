from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redismail.settings')

app = Celery('redismail')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Paris')

# CELERY BEAT SETTINGS

app.conf.beat_schedule = {
    'send-ad-mail-every-day': {
        'task': 'myapp2.tasks.send_ad_mails',
        'schedule': crontab(hour=15, minute=56),
        'args' : ("I am a Nigerian Prince.",)
    }
}

app.autodiscover_tasks()
