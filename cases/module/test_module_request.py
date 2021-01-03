# 学习目的：反向获取测试模块的属性
# 例子：跨域，测试用例不全是使用同一个环境


# 先指定跨域的地址，
# web_server为test_module_request.py这个模块中的一个属性，可在conftest.py中使用request.module反向获取该属性值
web_server = "https://www.cnblogs.com/"


def test_m(host_env):
    print("读取环境：%s" % host_env)
