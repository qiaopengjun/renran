import json
from urllib.parse import urlencode,parse_qs
from urllib.request import urlopen


class QQNetworkError(Exception):
    pass


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

    def get_access_token(self, code):
        """根据授权码获取access_token临时访问票据"""
        query_dict = {
            "grant_type": "authorization_code",
            "client_id": self.app_id,
            "client_secret": self.app_key,
            "code": code,
            "redirect_uri": self.redirect_uri,
        }
        query_string = urlencode(query_dict)
        url = "https://graph.qq.com/oauth2.0/token?" + query_string
        try:
            result = urlopen(url)
            content_string = result.read().decode()
            content_dict = parse_qs(content_string)
        except:
            raise QQNetworkError

        return content_dict["access_token"][0], content_dict["refresh_token"][0]

    def get_open_id(self, access_token):
        """根据临时访问票据获取QQ用户的openID"""
        query_dict = {
            "access_token": access_token,
            "fmt": "json",
        }
        query_string = urlencode(query_dict)
        url = "https://graph.qq.com/oauth2.0/me?" + query_string
        try:
            result = urlopen(url)
            content_string = result.read().decode()
            content_dict = json.loads(content_string)
        except:
            raise QQNetworkError

        return content_dict["openid"]
