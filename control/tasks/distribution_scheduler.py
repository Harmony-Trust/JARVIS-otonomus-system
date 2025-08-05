# 🚀 Distribution Scheduler - Celery Example

from celery import Celery
from integrations.supabase.supabase_client import store_payload

celery_app = Celery('jarvis_tasks', broker='redis://localhost:6379/0')

@celery_app.task
def distribute_content(table, data):
    return store_payload(table, data)