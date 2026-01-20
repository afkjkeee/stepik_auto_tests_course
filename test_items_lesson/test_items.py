from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    test_pass = False
    try:
        browser.find_element(
                    By.CSS_SELECTOR, "#add_to_basket_form > button")
        test_pass = True
    except:
        pass
    assert test_pass == True, "Button 'Add to basket' is missing on the page" 
