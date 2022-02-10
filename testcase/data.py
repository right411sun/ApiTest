#账号
user = [
        ("visitor", {"email": "shiyangyan1@163.com", "password": "password123"}),
        ("developer", {"email": "shiyangyan@163.com", "password": "password123"}),
        ("admin", {"email": "admin@admin.com", "password": "password123"})
]

#切换用户
user1 = ["visitor", "developer"]
user2 = ["admin", "developer"]

#查看接口
find_api = {
        "project_id":86
}


#正常添加接口
add_api_nromal= {
        "method":"GET",
        "catid":"132",
        "title":"api1",
        "path":"/api1",
        "project_id":86
}

#错误添加接口 path错误类型
add_api_error= {
        "method":"GET",
        "catid":"132",
        "title":"api1",
        "path":"哈哈哈",
        "project_id":86
}

#异常添加接口
add_api_null= {
        "method":"GET",
        "catid":"132",
        "title":"",
        "path":"",
        "project_id":86
}


#边界值错误添加接口
add_api_bound= {
        "method":"GET",
        "catid":"132",
        "title":"你"*100,
        "path":"/api14",
        "project_id":86
}

#修改接口
edit_api = {
        "req_query":[],
        "req_headers":[],
        "req_body_form":[],
        "title":"api2",
        "catid":"132",
        "path":"/api2",
        "tag":[],
        "status":"undone",
        "req_body_is_json_schema":"true",
        "res_body_is_json_schema":"true",
        "res_body_type":"json",
        "res_body":"",
        "switch_notice":"true",
        "api_opened":"false",
        "desc":"",
        "markdown":"",
        "method":"GET",
        "req_params":[],
        "id":""
}


#删除接口
del_api = {
        "id":""
}


