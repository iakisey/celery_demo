import datetime
import wechat_base_info

CELERYBEAT_SCHEDULE = {
    'periodic_task': {
        'task': 'tasks.periodic_task',
        'schedule': datetime.timedelta(seconds=10),
        'args': (wechat_base_info.update_access_token,)
    },
}
