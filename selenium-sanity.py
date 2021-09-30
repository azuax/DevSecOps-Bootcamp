from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


target_url = "http://devsecops.go-hacking.com/"

print("########## Running the Selenium Script ##########")

@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    yield
    driver.close()

@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_id("title")
    print("########## Checking for text ##########")
    assert element.text == "Hello, World!"
