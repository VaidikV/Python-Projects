import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

email = "[enteremail]"
password = "[enterpassword]"

s = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=106164952&keywords=python%20developer&lo"
           "cation=Mumbai%2C%20Maharashtra%2C%20India")
driver.maximize_window()
# Clicking the sign in button
driver.find_element(By.CSS_SELECTOR, "div .nav__button-secondary").click()

# Entering details
driver.find_element(By.CSS_SELECTOR, "div #username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "div #password").send_keys(password)

# signing in
driver.find_element(By.CSS_SELECTOR, "div .btn__primary--large.from__button--floating").click()

# following the job givers...or whatever they are called.
job_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for jb in range(0, 6):
    time.sleep(1)
    job_listings[jb].click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div .jobs-save-button").click()


