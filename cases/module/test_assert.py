# 同一测试用例中，失败的断言其后代码(包括其后的其他断言)不就会被执行
# 测试用例之间断言失败互不干扰
# 通过pytest插件: pytest-assume   进行断言可实行断言失败后继续执行其后代码
# 导入pytest包，使用pytest.assume(断言内容) 方法进行断言，替代python 中的assert断言
# 执行到失败的断言先不报错抛出异常，等运行完代码后再抛出异常(实际工作中很少用到这种方法，因为一旦断言失败就没必要再继续运行用例了)

import pytest
from pytest import assume


def test_a():
    print("1111111111")
    a = "hello"
    b = "hello world"
    print(a)

    # assert a == b
    # pytest.assume(a == b)
    # pytest.assume也可以使用上下文管理器去断言
    with assume: assert a == b
    with assume: assert a != b
    # 断言通过，后面的代码会继续
    print("断言失败后：%s" % b)

    # assert a in b
    pytest.assume(a in b)
    with assume: assert a in b
    # 断言通过，后面的代码会继续
    print("断言后：%s" % b)


def test_b():
    print("22222222222")
    a = "hello"
    b = "hello world"
