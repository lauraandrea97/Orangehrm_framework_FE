from behave import given, when, then
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@when('hace click en forgot your password')
def step_click_forgot_password(context):
    context.login_page.click_forgot_password()
    context.reset_page = ResetPasswordPage(context.driver)


@when('ingresa el username "{user}"')
def step_enter_reset_username(context, user):
    user = "" if user == "EMPTY" else user
    context.reset_page.enter_username(user)

@when('hace click en Reset Password')
def step_click_reset_password(context):
    context.reset_page.click_reset_password()


@then('debería ver el mensaje "{resultado}"')
def step_verify_reset_message(context, resultado):
    if resultado == "Reset Password link sent successfully":
        assert context.reset_page.is_success_message_visible()
    elif resultado == "mensajeerror":
        assert context.reset_page.is_reset_password_error_visible()
    else:
        raise ValueError(f"Resultado inválido: {resultado}")