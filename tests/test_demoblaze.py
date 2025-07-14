import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pom.login_page import LoginPage

@pytest.fixture(scope="module")
def setup_driver():
    service = Service(r"C:\Users\USER1\Downloads\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.demoblaze.com/")
    yield driver
    driver.quit()

def test_login_and_add_to_cart(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.login("Kolade31", "Kolade31") 