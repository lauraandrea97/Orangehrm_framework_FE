from behave import given, when, then
from pages.login_page import LoginPage
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


@given('el usuario está en la página de login')
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_login()


@when('ingresa credenciales "{user}" y "{password}"')
def step_enter_credentials(context, user, password):
    user = "" if user == "EMPTY" else user
    password = "" if password == "EMPTY" else password
    context.login_page.login(user, password)


@then('debería ver "{resultado}"')
def step_verify_resultado(context, resultado):
    if resultado == "dashboard":
        assert context.login_page.is_dashboard_visible()
    elif resultado == "mensajeerror":
        assert context.login_page.is_error_visible()
    else:
        raise ValueError(f"Resultado inválido: {resultado}")