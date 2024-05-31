import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "therock"
USERNAME = "[username]"
PASSWORD = "[password]"
# CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
# s = Service(CHROME_DRIVER_PATH)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Development\\chromedriver.exe")

    def login(self):
        login_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(login_url)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        log_in = self.driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/div/div[3]")
        log_in.click()

    def find_followers(self):
        time.sleep(4)
        similar_account_url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(similar_account_url)
        followers = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li"
                                                       "[2]/a")
        followers.click()
        time.sleep(5)
        focus = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]")

        # Scrolling
        for i in range(10):
            print(i)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;"
                                       , focus)
            time.sleep(2)

        follower_button_list = self.driver.find_elements(By.CSS_SELECTOR, "li button")

        print(len(follower_button_list))

    def follow(self):
        follower_button_list = self.driver.find_elements(By.CSS_SELECTOR, "li button")

        print(len(follower_button_list))
        for user in follower_button_list:
            try:
                user.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()


InstaFollower = InstaFollower()

InstaFollower.login()
InstaFollower.find_followers()
InstaFollower.follow()
