import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from behave import given
from pages.login_page import LoginPage


@given('el usuario está en la página de login')
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_login()