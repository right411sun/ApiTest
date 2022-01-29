import pytest
import requests
from config.config import *
from common.request import req

@pytest.fixture(scope='session', autouse=True)
def yapi_login():
    print('测试用例开始执行')
    date = user[0]
    res = requests.post(url=api_url + "/api/user/login", data=date)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    headers = {"Cookie": "_yapi_token=" + cookie["_yapi_token"] + ";" + "_yapi_uid=" + cookie["_yapi_uid"]}
    req.get_header(headers)
    yield
    print('测试用例执行结束')


