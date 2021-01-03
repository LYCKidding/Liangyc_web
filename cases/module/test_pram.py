import pytest

# data = [(1, 2), (2, 3)]
#
# @pytest.mark.parametrize("a, b", data)   # 测试用例数据的参数化
# def test_add(a, b):
#     print("a=", a)
#     print("b=", b)
#     return print("a+b=%s" % (a+b))





test_data = ["user1", "user2"]
# request 是pytest中内置的fixture，
# request.param只有在fixture中才能获取参数化fixture的参数化数据，在测试用例中无法使用

@pytest.fixture(params=test_data)
def register_users(request):
    user = request.param  # 获取测试数据
    print("拿着账号去注册：%s" % user)
    result = {"code": 0, "msg": "success"}
    return user, result


# 测试用例
def test_register(register_users):
    # 拿到前面的测试数据
    user, actual_result = register_users
    print("在测试用例里面里面获取到当前测试数据：%s" % user)
    print("实际结果：%s" % actual_result)
    assert actual_result["msg"] == "success"
