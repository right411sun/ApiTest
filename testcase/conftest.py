import pytest
from common.request import req


@pytest.fixture(scope= "session",autouse= True)
def yapi_login():
    print('测试用例开始执行')
    req.get_header()
    yield
    print('测试用例执行结束')

