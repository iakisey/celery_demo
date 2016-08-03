import celery
import celery_conf

app = celery.Celery(
    'tasks',
    backend='redis://redis',
    broker='redis://redis:6379'
)
app.config_from_object(celery_conf)
celery.platforms.C_FORCE_ROOT = True


@app.task
def task_process(func, *args, **kwargs):
    return func(*args, **kwargs)


@app.task
def periodic_task(func, *arg, **kwargs):
    return func(*arg, **kwargs)
