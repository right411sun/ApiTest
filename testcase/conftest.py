import pytest
from common.request import req


@pytest.fixture(scope= "session",autouse= True)
def yapi_login():
    print('测试用例开始执行')
    req.get_header()
    print(req.vp)
    yield
    print(list(req.vp.values()))
    print('测试用例执行结束')


