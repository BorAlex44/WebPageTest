import logging
import time
import pytest
import yaml
from test_page import OperationsHelper, TestSearchLocators

with open('test_data.yaml') as file:
    test_data = yaml.safe_load(file)


def test_placeholder_username(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_placeholder_text() == 'Username'


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
def test_placeholder_username_background_color(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    assert test_page.get_element_property(TestSearchLocators.ids['LOCATOR_PLACEHOLDER_USERNAME'],
                                          'background-color') == 'rgba(0, 0, 0, 0)'


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
