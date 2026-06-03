from selenium.webdriver.common.by import By
from .base_page import BasePage
from untils.config import BASE_URL


class LoginPage(BasePage):

# locatos
USERNAME_INPUT = (By.NAME, "username")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")


# Acciones login
def navigate_login(self):
    self.navigate_to(BASE_URL)
