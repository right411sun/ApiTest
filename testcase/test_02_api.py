#   写个接口测试demo  你需要维护token来保证需要登录才能访问的接口也能够正常访问
import pytest
from common.request import vp
from common.request import req
from testcase.data import *
from config.config import *



#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.parametrize("cookie",[vp["admin_cookie"], vp["developer_cookie"], vp["visitor_cookie"]])
def test_find_api(cookie):
    print('正在执行：查看接口')
    req.get_header(cookie)
    res = req.api_get("/api/interface/list_menu",params= find_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

#@pytest.mark.debug
@pytest.mark.syy
class Test_Add_Api():
    #添加接口

    @pytest.mark.parametrize("cookie", [vp["admin_cookie"], vp["developer_cookie"]])
    def test_add_normal(self, cookie):
        print('正在执行：正常添加接口')
        req.get_header(cookie)
        res = req.api_post("/api/interface/add", data=add_api_nromal)
        vp['api_id'] = res['res']['data']['_id']
        assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

    @pytest.mark.parametrize("cookie", [vp["admin_cookie"], vp["developer_cookie"]])
    def test_add_error(self, cookie):
        print('正在执行：错误添加接口') #path类型错误
        req.get_header(cookie)
        res = req.api_post("/api/interface/add", data=add_api_error)
        assert res['res']['errmsg'] == 'path第一位必需为 /, 只允许由 字母数字-/_:.! 组成', "实际返回数据:{}".format(str(res))

    @pytest.mark.parametrize("cookie", [vp["admin_cookie"], vp["developer_cookie"]])
    def test_add_null(self, cookie):
        print('正在执行：必填项置空添加接口')  #title，path置空
        req.get_header(cookie)
        res = req.api_post("/api/interface/add", data=add_api_null)
        assert res['res']['errmsg'] == '请求参数 data.path 不应少于 1 个字符\ndata.title 不应少于 1 个字符', "实际返回数据:{}".format(str(res))

    @pytest.mark.parametrize("cookie", [vp["admin_cookie"], vp["developer_cookie"]])
    def test_add_bound(self, cookie):
        print('正在执行：边界值错误添加接口')  # title超出字符
        req.get_header(cookie)
        res = req.api_post("/api/interface/add", data=add_api_bound)
        assert res['res']['errmsg'] == '请输入接口名称，长度不超过100字符(中文算作2字符)!', "实际返回数据:{}".format(str(res))

#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.parametrize("cookie",[vp["admin_cookie"], vp["developer_cookie"]])
# 修改接口
def test_edit_api(cookie):
    print('正在执行：修改接口')
    req.get_header(cookie)
    edit_api['id'] = vp['api_id']
    res = req.api_post("/api/interface/up", data=edit_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))

#@pytest.mark.debug
@pytest.mark.syy
@pytest.mark.parametrize("cookie",[vp["admin_cookie"], vp["developer_cookie"]])
# 删除接口
def test_del_api(cookie):
    print('正在执行：删除接口')
    req.get_header(cookie)
    del_api['id'] = vp['api_id']
    res = req.api_post("/api/interface/del", data=del_api)
    assert res['res']['errmsg'] == '成功！', "实际返回数据:{}".format(str(res))