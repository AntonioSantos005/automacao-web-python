from behave import *
from nose.tools import assert_equal
from pages.login_page import LoginPage
from pathlib import Path

loginPage = LoginPage()


@given(u'que acesso a pagina do Hrm')
def step_impl(context):
    loginPage.acess_page('https://opensource-demo.orangehrmlive.com/')
    print(Path.home())


@when(u'preencher o campo user com "{text}"')
def step_impl(context, text):
    loginPage.send_keys_input_username(text)


@when(u'preencher o campo senha com "{text}"')
def step_impl(context, text):
    loginPage.send_keys_input_password(text)


@when(u'clicar no botao login')
def step_impl(context):
    loginPage.click_button_login()


@then(u'o sistema apresenta o usuario logado "{text}"')
def step_impl(context, text):
    assert_equal(Path.home(), loginPage.get_text_user_logged())
