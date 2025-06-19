from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser


class LoginPageLocator(object):
    INPUT_USERNAME = '[name="txtUsername"]'
    INPUT_PASSWORD = '[name="txtPassword"]'
    BUTTON_LOGIN = '[name="Submit"]'
    TEXT_USER_LOGGED = '[id="welcome"]'


class LoginPage(Browser):
    def get_element(self, locator):
        # aguarda elemento estar visível na tela
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # retorna elemento
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        # acessa url passada
        self.driver.get(url)

    def send_keys_input_username(self, text):
        # envia para o elemento o texto 'Python'
        input_username = self.get_element(LoginPageLocator.INPUT_USERNAME)
        input_username.send_keys(text)

    def send_keys_input_password(self, text):
        # envia para o elemento o texto 'Python'
        input_password = self.get_element(LoginPageLocator.INPUT_PASSWORD)
        input_password.send_keys(text)

    def click_button_login(self):
        # clica no botão de pesquisar
        button = self.get_element(LoginPageLocator.BUTTON_LOGIN)
        button.click()

    def get_text_user_logged(self):
        # retorna o texto do elemento
        element = self.get_element(LoginPageLocator.TEXT_USER_LOGGED)
        return element.text
