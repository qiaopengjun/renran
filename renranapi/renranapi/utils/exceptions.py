from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging

logger = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
    自定义异常处理函数
    :param exc: 异常类对象
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)
    if response is None:
        view = context["view"]
        """当response的值为None，则有可能出现2种情况: 没有发生异常，或者本次异常没有被drf进行处理"""
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error("数据库发生异常。view=%s，exc=%s" % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
