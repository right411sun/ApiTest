#   写个接口测试demo  你需要维护token来保证需要登录才能访问的接口也能够正常访问
import pytest
from common.request import vp
from common.request import req
from testcase.data import *


#创建项目
@pytest.mark.debug
@pytest.mark.case
def test_add_projcet(yapi_login):
    print('正在执行：创建项目')
    if yapi_login == "访客账号":
        pytest.skip("访客账号没有权限,跳过该用例")
    res = req.api_post("/api/project/add",data= add_project)
    vp['prijcet_id'] = res['res']['data']['_id']
    assert res['res']['errmsg'] == '成功！'

#删除项目
@pytest.mark.debug
@pytest.mark.case
def test_del_project(yapi_login):
    print('正在执行：删除项目')
    if yapi_login == "访客账号":
        pytest.skip("访客账号没有权限,跳过该用例")
    del_projcet["id"] = vp['prijcet_id']
    res = req.api_post("/api/project/del", data= del_projcet)
    assert res['res']['errmsg'] == '成功！'



#@pytest.mark.debug
@pytest.mark.case
class Test_Api():

    # 添加接口
    def test_add_api(self,yapi_login):
        print('正在执行：添加接口')
        res = req.api_post("/api/interface/add", data=add_api)
        if yapi_login == "访客账号":
            assert res['res']['errmsg'] == '没有权限'
            return
        vp['api_id'] = res['res']['data']['_id']
        assert res['res']['errmsg'] == '成功！'


    #修改接口
    def test_edit_api(self,yapi_login):
        print('正在执行：修改接口')
        if yapi_login == "访客账号":
            pytest.skip("访客账号没有权限,跳过该用例")
        edit_api['id'] = vp['api_id']
        res = req.api_post("/api/interface/up", data=edit_api)
        assert res['res']['errmsg'] == '成功！'

    #删除接口
    def test_del_api(self,yapi_login):
        print('正在执行：删除接口')
        if yapi_login == "访客账号":
            pytest.skip("访客账号没有权限,跳过该用例")
        del_api['id'] = vp['api_id']
        res = req.api_post("/api/interface/del", data=del_api)
        assert res['res']['errmsg'] == '成功！'









