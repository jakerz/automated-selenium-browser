
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ChromeBrowser:
    def __init__(self, webpage_url, actions):
        self.webpage_url = webpage_url
        self.actions = actions

    def example_routine(self):
        self.load_webdriver()
        self.navigate_to_url()
        html_source = self.get_html_page_source()
        print(html_source[0:100])
        time.sleep(5)
        self.close()

    def load_webdriver(self):
        self.driver = webdriver.Chrome()

    def navigate_to_url(self, url=None):
        if url is None:
            url = self.webpage_url
        self.driver.get(url)

    def get_html_page_source(self):
        return self.driver.page_source

    def close(self):
        self.driver.close()
