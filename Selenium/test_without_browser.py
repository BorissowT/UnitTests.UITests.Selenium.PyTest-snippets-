link = "http://selenium1py.pythonanywhere.com/"

#pytest -s -v --browser_name=chrome Selenium\test...
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")