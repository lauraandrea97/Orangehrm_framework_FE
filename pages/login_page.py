from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT  = (By.NAME, "username")
    PASSWORD_INPUT  = (By.NAME, "password")
    LOGIN_BUTTON    = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_TITLE = (By.XPATH, "//h6[contains(.,'Dashboard')]")
    ERROR_MESSAGE   = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    FIELD_ERROR = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")

    # Acciones
    def navigate_login(self):
        self.navigate_to(BASE_URL)

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_dashboard_visible(self):
        return self.wait_for_element(self.DASHBOARD_TITLE).is_displayed()


    def is_error_visible(self):
        try:
            return self.wait_for_element(self.ERROR_MESSAGE).is_displayed()
        except:
            return self.wait_for_element(self.FIELD_ERROR).is_displayed()