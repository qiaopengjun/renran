def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :param token: jwt token字符串
    :param user: 本次成功登录的用户模型对象
    :param request: 本次登录用户的http请求对象
    :return: dict
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username if user.username else "暂无",
        'avatar': user.avatar.url if user.avatar else "",
    }
