from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# def test_open():
#     browser.get('https://suninjuly.github.io/xpath_examples')
#     browser.get('http://suninjuly.github.io/cats.html')
#     browser.find_element("//*[contains(text(), 'Bullet cat')]")
# time.sleep(5)

def open_page():
    browser.get('http://suninjuly.github.io/cats.html')    # открыли сайт
    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")    # нашли элемент по XPATH
    print(bullet_cat.text)

    view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_buttons)
    assert len(view_buttons) == 6, 'Wrong length'

def test_open_page():
    open_page()
