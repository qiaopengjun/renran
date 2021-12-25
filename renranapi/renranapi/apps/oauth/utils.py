from urllib.parse import urlencode


class OAuthQQ(object):
    """QQ登录工具类"""

    def __init__(self, app_id, app_key, redirect_uri, state="/"):
        self.app_id = app_id
        self.app_key = app_key
        self.redirect_uri = redirect_uri
        self.state = state

    def url(self):
        """生成QQ登录地址"""
        query_dict = {
            "response_type": "code",  # 授权类型，此值固定为“code”。
            "client_id": self.app_id,  # 申请QQ登录成功后，分配给应用的appid。
            # 成功授权后的回调地址，必须是注册appid时填写的主域名下的地址，建议设置为网站首页或网站的用户中心。注意需要将url进行URLEncode。
            "redirect_uri": self.redirect_uri,
            # client端的状态值。用于第三方应用防止CSRF攻击，成功授权后回调时会原样带回。请务必严格按照流程检查用户与state参数状态的绑定。
            "state": self.state,
        }
        query_string = urlencode(query_dict)

        return "https://graph.qq.com/oauth2.0/authorize?" + query_string
