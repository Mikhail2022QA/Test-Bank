import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setup(requests):
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(2)
    browser.set_window_size(1920, 1080)
    request.cls.driver = browser
    yield browser
    browser.close()