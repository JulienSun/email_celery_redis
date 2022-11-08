from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
import email_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_redis.settings")

app = Celery("celery_redis")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "add-every-5-seconds": {
        "task": "email_app.tasks.send_email",
        "schedule": 5,
        "args": (16, 16),
    },
}


# @app.on_after_configure.connect  # 启动程序连接上celery后自动执行这个函数生成定时任务
# def setup_periodic_tasks(sender, **kwargs):  # 第一次参数必须是sender,是定时任务的一个实例
#     # Calls test('hello') every 10 seconds.   这里的test是我们自定义的函数
#     print("add periodic task")
#     sender.add_periodic_task(
#         10.0, email_app.tasks.send_email.s("hello"), name="add every 10"
#     )

# Calls test('world') every 30 seconds
# sender.add_periodic_task(30.0, debug_task.s('world'), expires=10)

# Executes every Monday morning at 7:30 a.m.  更复杂的定时任务
# sender.add_periodic_task(
#     crontab(hour=7, minute=30, day_of_week=1),
#     test.s('Happy Mondays!'),
# )


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
