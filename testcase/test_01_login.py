import pytest
import requests
from common.request import vp
from common.request import req
from config.config import *
from testcase.data import *

#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.parametrize("user_type, user_data", user)
def test_login(user_type, user_data):
    """登陆"""
    print("正在执行：{}账号登陆".format(user_type))
    res = req.api_post("/api/user/login", data= user_data)
    vp["{}_cookie".format(user_type)]  = \
        {"Cookie":"_yapi_token=" + res['cookie']["_yapi_token"] +";" + "_yapi_uid=" + res['cookie']["_yapi_uid"]}
    assert res['res']['errmsg'] == 'logout success...', "实际返回数据:{}".format(str(res))
