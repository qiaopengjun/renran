from mycelery.main import app
from celery.schedules import crontab
from django.conf import settings

# 任务队列的链接地址
broker_url = 'redis://127.0.0.1:6379/15'
# 结果队列的链接地址
result_backend = 'redis://127.0.0.1:6379/14'

# 和django框架同步时区

app.conf.timezone = settings.TIME_ZONE

app.conf.beat_schedule = {
    # 定时任务列表
    'pub-article-every-two-minute': {
        'task': 'interval_pub_article',  # 指定定时执行的的异步任务
        # 'schedule': crontab(),            # 时间间隔,一分钟
        # 'schedule': 120.0,                # 时间间隔,默认:秒
        'schedule': crontab(minute='*/2'),  # 时间间隔,每2分钟
        # 'args': (16, 16)                  # 如果任务有固定参数,则可以写在args
    },
}
