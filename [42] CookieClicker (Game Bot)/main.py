import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

s = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")


def buy_buildings():
    cookies = driver.find_element(By.ID, "cookies")

    try:
        cookie_count = int(cookies.text.split()[0])
    except ValueError:
        cookie_count = int(cookies.text.split()[0].replace(",", ""))

    building_price_int = []
    buildings = driver.find_elements(By.CLASS_NAME, "unlocked")
    building_price_str = [item.text.split("\n")[1] for item in buildings]

    # Removing "," from the prices in buildings section and converting to int data type.
    for price in building_price_str:
        try:
            building_price_int.append(int(price))
        except ValueError:
            building_price_int.append(int(price.replace(",", "")))

    try:
        if building_price_int[-1] + building_price_int[-2] + building_price_int[-3] < cookie_count:
            buildings[-1].click()
            buildings[-2].click()
            buildings[-3].click()
        else:
            pass
    except IndexError:
        if building_price_int[-1] + building_price_int[-2] < cookie_count:
            buildings[-1].click()
            buildings[-2].click()
        else:
            pass


def click_goodies():
    # For clicking golden cookies & reindeers
    try:
        goodies = driver.find_element(By.CSS_SELECTOR, "#shimmers .shimmer")
        goodies.click()
    except NoSuchElementException:
        pass


def buy_upgrades():
    try:
        upgrades = driver.find_element(By.CSS_SELECTOR, "#upgrades .enabled")
        upgrades.click()
    except NoSuchElementException:
        pass


def disable_notifications():
    try:
        driver.find_element(By.CLASS_NAME, "sidenote").click()
    except NoSuchElementException:
        pass


# Changing settings
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".cc_banner .cc_btn").click()
driver.find_element(By.ID, "prefsButton").click()
time.sleep(2)
driver.find_element(By.ID, "monospaceButton").click()
time.sleep(2)
driver.find_element(By.ID, "formatButton").click()
time.sleep(2)
driver.find_element(By.ID, "prefsButton").click()

game_start_time = time.time()
building_start_time = time.time()
upgrade_start_time = time.time()
game_on = True

# Driver code
while game_on:
    try:
        cookie.click()
    except ElementClickInterceptedException:
        pass
    if time.time() - building_start_time > 4:
        buy_buildings()
        click_goodies()
        disable_notifications()
        building_start_time = time.time()
    elif time.time() - upgrade_start_time > 2:
        buy_upgrades()
        upgrade_start_time = time.time()
    elif time.time() - game_start_time > 300:
        per_sec_element = driver.find_element(By.ID, "cookies")
        per_second = per_sec_element.text.split("\n")[1]
        print(f"Cookies {per_second}")
        game_on = False
