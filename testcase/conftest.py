import pytest
import requests
from config.config import *
from common.request import req
from common.request import vp
import sys



@pytest.fixture(scope= "session",autouse= True)
def yapi_login():
    for i in user:
        res = requests.post(url=api_url + "/api/user/login", data=i['user_name'])
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        header = {"Cookie": "_yapi_token=" + cookie["_yapi_token"] + ";" + "_yapi_uid=" + cookie["_yapi_uid"]}
        vp["{}_cookie".format(i['user_type'])] = header

    print('{}账号测试用例开始执行'.format(sys.argv[2]))
    print("vp存储池检查中... {}".format(vp))
    req.get_header(vp["{}_cookie".format(sys.argv[2])])
    yield
    print('{}账号测试用例执行结束'.format(sys.argv[2]))


