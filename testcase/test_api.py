#   写个接口测试demo  你需要维护token来保证需要登录才能访问的接口也能够正常访问
import pytest
from common.request import req
from testcase.data import *

@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.run(order=2)
@pytest.mark.parametrize('user_type',user1)
def test_find_api(user_type):
    print('正在执行：查看接口')
    req.get_header(req.vp["{}_cookie".format(user_type)])
    res = req.api_get("/api/interface/list_menu", params= find_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.run(order=2)
class Test_Add_Api():
    #添加接口
    def test_add_normal(self):
        print('正在执行：正常添加接口')
        res = req.api_post("/api/interface/add", data=add_api_nromal)
        req.vp['api_id'] = res['res']['data']['_id']
        assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

    @pytest.mark.parametrize('user_type',user2)
    def test_add_error(self,user_type):
        print('正在执行：错误添加接口') #path类型错误
        req.get_header(req.vp["{}_cookie".format(user_type)])
        res = req.api_post("/api/interface/add", data=add_api_error)
        assert res['res']['errmsg'] == 'path第一位必需为 /, 只允许由 字母数字-/_:.! 组成', "实际返回数据:{}".format(str(res))

    def test_add_null(self):
        print('正在执行：必填项置空添加接口')  #title，path置空
        res = req.api_post("/api/interface/add", data=add_api_null)
        assert res['res']['errmsg'] == '请求参数 data.path 不应少于 1 个字符\ndata.title 不应少于 1 个字符', "实际返回数据:{}".format(str(res))

    def test_add_bound(self):
        print('正在执行：边界值错误添加接口')  # title超出字符
        res = req.api_post("/api/interface/add", data=add_api_bound)
        assert res['res']['errmsg'] == '请输入接口名称，长度不超过100字符(中文算作2字符)!', "实际返回数据:{}".format(str(res))

# 修改接口
#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.run(order=2)
def test_edit_api():
    print('正在执行：修改接口')
    edit_api['id'] = req.vp['api_id']
    res = req.api_post("/api/interface/up", data=edit_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

# 删除接口
#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.run(order=2)
def test_del_api():
    print('正在执行：删除接口')
    del_api['id'] = req.vp['api_id']
    res = req.api_post("/api/interface/del", data=del_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))