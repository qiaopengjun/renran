import json
import logging
from mycelery.main import app
# from celery.task import Task
from celery import Task
from ronglian_sms_sdk import SmsSDK
from django.conf import settings
from renranapi.settings import constants


# 监听整个任务的钩子
class Mytask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task success 11111')
        return super(Mytask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task failed')
        # 可以记录到程序中或者任务队列中,让celery尝试重新执行
        return super(Mytask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('this is after return')
        return super(Mytask, self).after_return(status, retval, task_id, args, kwargs, einfo)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print('this is retry')
        return super(Mytask, self).on_retry(exc, task_id, args, kwargs, einfo)


logger = logging.getLogger("django")


@app.task(name="send_sms", base=Mytask)
def send_sms(mobile, sms_code):
    """发送短信验证码"""
    # 实例化短信接口SDK对象
    try:
        sdk = SmsSDK(settings.SMS["accId"], settings.SMS["accToken"], settings.SMS["appId"])
        # 短信模板中的数据: 测试模板格式: 云通讯】您的验证码是{1}，请于{2}分钟内正确输入。
        datas = (sms_code, constants.SMS_EXPIRE_TIME // 60)
        resp = sdk.sendMessage(settings.SMS["tid"], mobile, datas)
        resp = json.loads(resp)
        if resp.get("statusCode") != "000000":
            # 记录错误信息
            logger.error("发送短信失败!手机号:%s" % mobile)
            raise Exception("发送短信失败!")
        else:
            return {"detail": "发送短信成功"}
    except:
        raise Exception("发送短信失败!")
