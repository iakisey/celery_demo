import celery

app = celery.Celery(
    'tasks',
    backend='redis://localhost',
    broker='redis://localhost:6379'
)
app.config_from_object('celery_conf')


@app.task
def task_process(func, *args, **kwargs):
    return func(*args, **kwargs)


@app.task
def periodic_task(func, *arg, **kwargs):
    return func(*arg, **kwargs)
