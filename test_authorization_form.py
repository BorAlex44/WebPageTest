import logging
import time
import pytest
import yaml
from test_page import OperationsHelper, TestSearchLocators

with open('test_data.yaml') as file:
    test_data = yaml.safe_load(file)


def test_displays_username_field(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.find_element('LOCATOR_FIELD_LOGIN')
    assert True


def test_placeholder_username(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_placeholder_username_text() == 'Username'


def test_placeholder_username_before(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('')
    assert test_page.get_placeholder_text_before() == ''


def test_placeholder_username_font_size(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_USERNAME'],
                                          'font-size') == '16px'


def test_placeholder_username_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_USERNAME'],
                                          'color') == 'rgba(0, 0, 0, 0.6)'


def test_placeholder_username_font_weight(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_USERNAME'],
                                          'font-weight') == '400'


def test_username_field_background_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_USERNAME_FIELD'],
                                          'background-color') == 'rgba(245, 245, 245, 1)'


def test_username_field_height(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_USERNAME_FIELD'],
                                          'height') == '56px'


def test_username_field_width(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_USERNAME_FIELD'],
                                          'width') == '360px'


def test_username_field_padding(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_USERNAME_FIELD'],
                                          'padding') == '0px 16px'


def test_username_input_field_height(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_INPUT_FIELD'],
                                          'height') == '28px'


def test_username_input_field_width(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_INPUT_FIELD'],
                                          'width') == '328px'


def test_input_username_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('Test')
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_INPUT_FIELD'],
                                          'color') == 'rgba(0, 0, 0, 0.87)'


def test_displays_password_field(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.find_element('LOCATOR_PASSWORD_FIELD')
    assert True


def test_placeholder_password(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_placeholder_password_text() == 'Password'


def test_placeholder_password_before(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_pass('')
    assert test_page.get_placeholder_password_text_before() == ''


def test_placeholder_password_font_size(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_PASSWORD'],
                                          'font-size') == '16px'


def test_placeholder_password_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_PASSWORD'],
                                          'color') == 'rgba(0, 0, 0, 0.6)'


def test_placeholder_password_font_weight(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_PASSWORD'],
                                          'font-weight') == '400'


def test_password_field_background_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_FIELD'],
                                          'background-color') == 'rgba(245, 245, 245, 1)'


def test_password_field_height(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_FIELD'],
                                          'height') == '56px'


def test_password_field_width(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_FIELD'],
                                          'width') == '360px'


def test_password_field_padding(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_FIELD'],
                                          'padding') == '0px 16px'


def test_password_input_field_height(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_INPUT_FIELD'],
                                          'height') == '28px'


def test_password_input_field_width(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_INPUT_FIELD'],
                                          'width') == '328px'


def test_input_password_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('Test')
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PASSWORD_INPUT_FIELD'],
                                          'color') == 'rgba(0, 0, 0, 0.87)'


def test_displays_button_login(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.find_element('LOCATOR_LOGIN_BTN')
    assert True


def test_button_login_background_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'],
                                          'background-color') == 'rgba(255, 62, 0, 1)'


def test_button_login_height(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], 'height') == '36px'


def test_button_login_width(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], 'width') == '360px'

def test_button_login_text(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_login_button_text() == 'LOGIN'

def test_button_login_text_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_BUTTON_TEXT'],
                                          'color') == 'rgba(255, 255, 255, 1)'

def test_button_login_text_font_size(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_LOGIN_BUTTON_TEXT'],
                                          'font-size') == '14px'
def test_step_1(browser):
    logging.info('Test-1  starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == '401'


def test_step_2(browser):
    logging.info('Test-2 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('')
    test_page.enter_pass(test_data.get('password'))
    test_page.click_login_button()
    time.sleep(test_data.get('sleep_time'))
    assert test_page.get_error_text() == '401'


def test_step_3(browser):
    logging.info('Test-3 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(test_data.get('login'))
    test_page.enter_pass('')
    test_page.click_login_button()
    time.sleep(test_data.get('sleep_time'))
    assert test_page.get_error_text() == '401'


def test_step_4(browser):
    logging.info('Test-4 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(test_data.get('login'))
    test_page.enter_pass(test_data.get('password'))
    test_page.click_login_button()
    time.sleep(test_data.get('sleep_time'))
    assert test_page.select_hello_user() == f'Hello, {test_data.get("login")}'


if __name__ == '__main__':
    pytest.main(['-vv'])
