from app import create_app
from celery_config import celery
import tasks

app = create_app()