from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    # Locators
    USERNAME_INPUT  = (By.NAME, "username")
    RESET_BUTTON    = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//h6[contains(.,'Reset Password link sent successfully')]")
    RESET_ERROR_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")


    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def click_reset_password(self):
        self.click(self.RESET_BUTTON)

    def is_success_message_visible(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).is_displayed()


    def is_reset_password_error_visible(self):
        return self.wait_for_element(self.RESET_ERROR_MESSAGE).is_displayed()