from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

webpage_url = "http://www.python.org"
webpage_url = "https://www.nadex.com"

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(webpage_url)
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
time.sleep(1)
# elem.clear()
# elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "No results found." not in driver.page_source
driver.close()


