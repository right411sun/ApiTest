#   写个接口测试demo  你需要维护token来保证需要登录才能访问的接口也能够正常访问
import pytest
from common.request import vp
from common.request import req
from testcase.data import *


#创建项目
@pytest.mark.debug
@pytest.mark.case
def test_add_projcet():
    print('正在执行：创建项目')
    res = req.api_post("/api/project/add",data= add_project)
    assert res['res']['errmsg'] == '成功！'



#@pytest.mark.debug
@pytest.mark.case
class Test_Api():
    # 添加接口
    def test_add_api(self):
        print('正在执行：添加接口')
        res = req.api_post("/api/interface/add", data=add_api)
        vp['api_id'] = res['res']['data']['_id']
        assert res['res']['errmsg'] == '成功！'


    #修改接口
    def test_edit_api(self):
        print('正在执行：修改接口')
        edit_api['id'] = vp['api_id']
        res = req.api_post("/api/interface/up", data=edit_api)
        assert res['res']['errmsg'] == '成功！'

    #删除接口
    def test_del_api(self):
        print('正在执行：删除接口')
        del_api['id'] = vp['api_id']
        res = req.api_post("/api/interface/del", data=del_api)
        assert res['res']['errmsg'] == '成功！'









