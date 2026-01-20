import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose your language: en/ru/fr/...")
    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options() 
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #options.add_argument(f"--lang={user_language}")
    browser = webdriver.Chrome(options=options)
    print("\nStart browser for test..")
    yield browser
    print("\nQuit browser..")
    browser.quit()
