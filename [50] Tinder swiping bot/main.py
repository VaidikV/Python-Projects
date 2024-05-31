import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

s = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/")
driver.maximize_window()

# Signing in
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id=\"u1186853273\"]/div/div[2]/div/div/div[1]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"u1186853273\"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]"
                              "/div[2]/a").click()
time.sleep(1)
try:
    driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div[1]/div/div[3]/span/div[2]/button").click()
except NoSuchElementException:
    driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div[1]/div/div[3]/span/button").click()
    print("clicked more options...waiting 5 secs")
    driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div[1]/div/div[3]/span/div[2]/button").click()
    print("clicked facebook button")
finally:
    time.sleep(2)

tinder_window = driver.window_handles[0]
fb_login_page = driver.window_handles[1]

driver.switch_to.window(fb_login_page)
print(driver.title)

time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("email")
driver.find_element(By.NAME, "pass").send_keys("pass")
driver.find_element(By.NAME, "login").click()

driver.switch_to.window(tinder_window)
print(driver.title)
time.sleep(8)
driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div/div/div[3]/button[1]/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div/div/div[3]/button[2]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id=\"u1408193709\"]/div/div/div/div[3]/button[2]/span").click()
time.sleep(8)
for swipe in range(1, 101):
    try:
        driver.find_element(By.XPATH, "//*[@id=\"u1186853273\"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/"
                                      "div[4]/div/div[4]/button/span/span").click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
    time.sleep(4)
