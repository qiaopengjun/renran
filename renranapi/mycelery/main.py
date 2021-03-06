# 主程序
import os
from celery import Celery

# 创建celery实例对象
app = Celery("renran")

# 把celery和django进行组合，必须让celery能识别和加载django的配置文件以及django的类库
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'renranapi.settings.dev')

# 对django框架执行初始化
import django

django.setup()

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.sms", "mycelery.email", "mycelery.article"])

# 启动Celery的命令
# 切换目录到mycelery上一级目录下启动
# celery -A mycelery.main worker --loglevel=info
# celery -A mycelery.main worker --loglevel=info
