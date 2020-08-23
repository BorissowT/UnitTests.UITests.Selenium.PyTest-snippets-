import time


class TestLanguage:
    def test_if_basket_exist(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        basket = None
        try:
            basket = browser.find_element_by_css_selector(".btn-add-to-basket")
        finally:
            assert basket, "basket not found"
        time.sleep(5)

