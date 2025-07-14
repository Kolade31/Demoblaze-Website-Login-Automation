from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.ID, "login2")  
        self.username_input = (By.ID, "loginusername")
        self.password_input = (By.ID, "loginpassword")
        self.submit_button = (By.XPATH, "//button[contains(text(), 'Log in')]")

    def login(self, username, password):
        self.driver.find_element(*self.login_button).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        self.driver.find_element(*self.submit_button).click()