from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver                          #prepara el navegador 
        self.wait = WebDriverWait(driver, timeout) 


    def navigate_to(self, url):           
        if not url:
            raise ValueError("URL no puede estar vacía")
        self.driver.get(url)     