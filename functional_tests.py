from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_argument("--no-sandbox")
driver = Chrome(options=options)
driver.get('http://localhost:8000')

assert 'Django' in driver.title 