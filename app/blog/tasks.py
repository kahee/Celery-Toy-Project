from celery import shared_task

from config.celery import app


@app.task(bind=True)
def blog_debug_task(self):
    return 'blog'


@shared_task
def blog_shared_task():
    return 'shared'
