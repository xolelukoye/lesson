from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options #для запуска браузера в гитхаб

@pytest.fixture()
def browser():
    options = Options() #для запуска браузера в гитхаб
    options.add_argument('--headless') #запуск браузера в безголовом (невидимом) режиме, для гитхаба
    browser = webdriver.Firefox(options=options) #options=options - для запуска в гитхаб
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()