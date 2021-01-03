import pytest


# 添加pytest命令行参数 "--host"
# pytest_addoption是个添加pytest命令行参数的hook函数，且该函数名称固定，并固定传入parser参数
# 可以将测试用的url动态添加到命令行参数中或者pytest.ini文件中
def pytest_addoption(parser):
    # 添加命令行参数
    parser.addoption(
        "--host", action="store", default="test", help="option: test or uat or pre"
    )
    # 添加pytest.ini参数
    parser.addini(
        name="user", type=None, default="admin", help="pytest.ini: test user"
    )


# 示例1：通过request获取从命令行传入的参数值
@pytest.fixture()
def host_env(request):
    env = request.config.getoption("--host")  # 获取从命令行传入的"--host" 参数值
    if env == "test":
        url = "http://49.235.92.12:8200/"
    elif env == "uat":
        url = "https://www.baidu.com/"
    else:
        url = "http://49.235.92.12:8200/"

    # 反向获取测试模块的属性：反向获取test_module_request.py 中web_server属性值，如果该属性值为空，返回url
    server = getattr(request.module, "web_server", url)
    return server


# 示例2: 使用 pytestconfig 获取从命令行传入的参数值
@pytest.fixture()
def get_env(pytestconfig):
    env = pytestconfig.getoption("--host")


# 示例3：使用 getini() 从 pytest.ini 配置文件获取参数
@pytest.fixture(scope="session", autouse=True)
def get_ini(pytestconfig):
    cmdopts = pytestconfig.getini("addopts")
    print("读取ini配置的内容：%s" % cmdopts)


# 使用pytestconfig.getini()方法读取到pytest.ini文件中创建的自定义参数值
@pytest.fixture(scope="session", autouse=True)
def get_user(pytestconfig):
    user = pytestconfig.getini("user")
    print("读取到ini文件中的user：%s" % user)