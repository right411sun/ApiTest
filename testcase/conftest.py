import pytest
import requests
from config.config import *
from common.request import req

@pytest.fixture(scope= "session",autouse= True,params= user)
def yapi_login(request):
    print('{}测试用例开始执行'.format(request.param['user_type']))
    res = requests.post(url= api_url + "/api/user/login", data= request.param['user_name'])
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    headers = {"Cookie": "_yapi_token=" + cookie["_yapi_token"] + ";" + "_yapi_uid=" + cookie["_yapi_uid"]}
    req.get_header(headers)
    yield request.param['user_type']
    print('{}测试用例执行结束'.format(request.param['user_type']))


