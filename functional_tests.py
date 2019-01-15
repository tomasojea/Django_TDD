from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import unittest
options = ChromeOptions()
options.add_argument("--no-sandbox")
browser.get('http://localhost:8000')

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = Chrome(options=options)

    def TearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
