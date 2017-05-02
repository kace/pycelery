from celery import Celery

# celery -A tasks worker --loglevel=info
#
# from tasks import add
# add.delay(4,4)

app = Celery('tasks', broker='pyamqp://guest@localhost//')
@app.task
def add(x, y):
    return x + y
