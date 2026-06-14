import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def before_scenario(context, scenario):
    browser = context.config.userdata.get("BROWSER", "chrome").lower()

    # True en GitHub Actions, False en tu computador local
    en_ci = os.getenv("CI", "false") == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if en_ci:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        if en_ci:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        context.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Browser '{browser}' no soportado")

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


def before_tag(context, tag):
    if tag == "smoke":
        print("Ejecutando pruebas smoke")
    if tag == "regression":
        print("Ejecutando suite de regresión")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        context.driver.save_screenshot(f"screenshots/{scenario.name}.png")
    context.driver.quit()


def after_all(context):
    print("Suite de pruebas finalizada")
