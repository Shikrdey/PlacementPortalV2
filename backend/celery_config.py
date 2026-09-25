from celery import Celery
from celery.schedules import crontab

celery = Celery("placement_portal", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

celery.conf.timezone = "Asia/Kolkata"

def init_celery(app):
    class FlaskTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = FlaskTask

celery.conf.beat_schedule = {
    "daily-reminder": {
        "task": "tasks.daily_reminder",
        "schedule": crontab(hour=9, minute=0),
    },
    "monthly-report": {
        "task": "tasks.monthly_report",
        "schedule": crontab(day_of_month=1, hour=9, minute=0),
    },
    "close-expired-drives": {
        "task": "tasks.close_expired_drives",
        "schedule": crontab(hour=0, minute=1), 
    }
}