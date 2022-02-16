from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="D:\drivers\chromedriver_win32\chromedriver.exe")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="D:\drivers\geckodriver-v0.30.0-win64\geckodriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#html report configuration
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'Tanishk'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Packages",None)
    metadata.pop("Plugins", None)





