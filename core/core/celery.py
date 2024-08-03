import os
from celery import Celery

from accounts.tasks import sendEmail

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


'''
# NOT used --> instead use 'django_celery_beat'

@app.on_after_configure.connect
def setup_periodic_tasks_(sender, **kwargs):
    sender.add_periodic_task(5, sendEmail.s(), name='send email every 5 seconds')

'''