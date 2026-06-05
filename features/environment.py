import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def before_scenario(context, scenario):
    browser = context.config.userdata.get("BROWSER", "chrome").lower()

    if browser == "chrome":
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        context.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
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
        context.driver.save_screenshot(f"screenshots/{scenario.name}.png")
    context.driver.quit()

def after_all(context):
    print("Suite de pruebas finalizada")

