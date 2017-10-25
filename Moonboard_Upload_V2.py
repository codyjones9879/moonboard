

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('D:/chromedriver.exe')
# load the page
driver.get("https://moonboard.com/Account/Login")

# get the submit button
bt_submit = driver.find_element_by_css_selector("[type=submit]")

# wait for the user to click the submit button (check every 1s with a 1000s timeout)
WebDriverWait(driver, timeout=9000, poll_frequency=1) \
  .until(EC.staleness_of(bt_submit))

print "submitted"

problemsButton = driver.find_element_by_id("m-viewproblem")
problemsButton.click()

print problemsButton