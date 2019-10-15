import time
import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_exist(browser):
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), \
        'Button "Add to basket" was NOT found'
