from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_open():
    browser.get('https://suninjuly.github.io/xpath_examples')
time.sleep(5)


