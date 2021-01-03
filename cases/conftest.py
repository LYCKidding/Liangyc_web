from selenium import webdriver
import pytest
from pages.user_login_page import UserLoginPage


@pytest.fixture(scope="session", name="driver")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()  # 最大化窗口
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "http://49.235.92.12:8200"


@pytest.fixture(scope="session")
def login_instance(driver, base_url):
    login_ins = UserLoginPage(driver, base_url)
    return login_ins
