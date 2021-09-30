from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pytest
import os


target_url = "http://devsecops.go-hacking.com/"

print("########## Running the Selenium Script ##########")

@pytest.fixture(scope="session")
def get_driver():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.binary_location = '/usr/bin/firefox'
    # binary = FirefoxBinary('/usr/bin/firefox')

    driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(), 'geckodriver'), options=options)
    yield
    driver.close()

@pytest.mark.usefixtures("get_driver")
def test_data():
    driver.get(target_url)
    element = driver.find_element_by_id("title")
    print("########## Checking for text ##########")
    assert element.text == "Hello, World!"
