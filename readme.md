# 项目描述

这是web的自动化项目，基于selenium+pytest框架

# 环境淮备

1.python 3.6
2.pytest 4.5.0

依赖包安装
> pip install -r requirements.txt

# 运行用例
> pytest

# 生成报告

> pytest --alluredir ./allure_report

# pytest.ini配置

pytest.ini配置的描述

```
[pytest]

log_cli = 1
;addopts = --alluredir ./allure_report
;testpaths = cases/module
;python_file = test_*.py

```

