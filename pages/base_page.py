from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException



class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver                          #prepara el navegador 
        self.wait = WebDriverWait(driver, timeout) 


    def navigate_to(self, url):           
        if not url:
            raise ValueError("URL no puede estar vacía")
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)     # Espera a que el elemento sea visible
        )

    def click(self, locator):
        try:
            element = self.wait.until(                     # Click seguro: Espera a que el elemento sea clickeable
                EC.element_to_be_clickable(locator)
            )
            # Hace scroll hasta el elemento
            self.driver.execute_script(                     # Ejecuta JavaScript desde Selenium.
                "arguments[0].scrollIntoView({block: 'center'});", element   # arguments[0] -Representa el elemento enviado desde Python.
            )                                                                # scrollIntoView() -Hace scroll automático hasta el elemento.
                                                                             # Centra el elemento en pantalla para evitar problemas visuales.
            try:
                element.click()                                         # hace click otra vez normal Usuario virtual → mouse → click visual
            except ElementClickInterceptedException:                     # Si algo bloquea el click (popup, overlay, etc.)
                self.driver.execute_script("arguments[0].click();", element)  # JavaScript → fuerza click directamente

        except TimeoutException:
            print(f"Elemento tardó demasiado: {locator}")
            raise

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)  # Click seguro: Espera a que el elemento sea visible
        element.clear()                            # Limpiar el campo, evita datos sucios
        element.send_keys(text)


    def navigate_to_reset(self):
        self.navigate_to(self.RESET_URL)