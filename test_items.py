import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_displayed(browser):
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed(), \
        'Button "Add to basket" was NOT found'
