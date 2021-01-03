import pytest
# 目的：在测试用例中传入命令行参数值

# 当测试用例需要使用到命令行参数"--host"值时，可以使用requestrequest.config.getoption("--host")获取
def test_host_1(request):
    env = request.config.getoption("--host")
    print("case env: %s" % env)

# 也可以使用自动以的获取命令行参数"--host"值的fixture
def test_host_2(host_env):
    print("case env: %s" % host_env)
