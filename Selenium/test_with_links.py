import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


links = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    answer = math.log(int(time.time()))
    actual_link = f"{link}"
    browser.get(actual_link)
    textarea = browser.find_element_by_css_selector(".textarea")
    textarea.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    respond = browser.find_element_by_css_selector(".smart-hints__hint")
    assert respond.text == "Correct!", f"{respond.text}"


a