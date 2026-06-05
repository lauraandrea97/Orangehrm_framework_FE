from behave import given, when, then
from pages.login_page import LoginPage


@when('hace click en forgot you password')
def step_click_forgot_password(context):
    context.login_page.click_forgot_password()

@then('debería ver el modal de Reset Password')
def step_verify_reset_modal(context):
    assert context.login_page.is_reset_password_visible()