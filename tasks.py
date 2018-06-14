import time

from celery import Celery

# Celery 인스턴스 생성
app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)

# 등록된 작업 처리
@app.task
def add(x, y):
    time.sleep(5)
    return x + y
