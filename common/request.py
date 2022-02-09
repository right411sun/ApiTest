import requests
from config.config import *


vp = {}

class Request():
    """
    封装通用方法
    """
    def get_header(self, header = {}):
        """
        获取headers
        """

        self.headers = header

    def api_get(self,url,params = ''):
        """
        封装get请求
        """
        try:
            res = requests.get(url= api_url + url,headers= self.headers,params= params)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            response = {"res": res.json(), "status_code": res.status_code, "cookie": cookie}
            print(response)
            return response
        except Exception as e:
            print('get请求失败,异常信息：{}'.format(e))

    def api_post(self,url,data):
        """
        封装post请求
        """
        try:
            res = requests.post(url= api_url + url, headers= self.headers, data= data)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            response = {"res": res.json(), "status_code": res.status_code, "cookie": cookie}
            print(response)
            return response
        except Exception as e:
            print('post请求失败,异常信息：{}'.format(e))


req = Request()