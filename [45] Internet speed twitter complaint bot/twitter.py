import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TWITTER_EMAIL = "[enteryouremail]"
TWITTER_PASSWORD = "[enterpassword]"

path = "C:\\Development\\chromedriver.exe"
s = Service(path)


class Twitter:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome(service=s)
        self.down = down
        self.up = up

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        sign_in = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]"
                                                     "/div/div[3]/div[5]/a/div")
        sign_in.click()
        time.sleep(6)
        email = self.driver.find_element(By.XPATH,
                                         "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/"
                                         "div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        next_form = self.driver.find_element(By.XPATH,
                                             "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div"
                                             "[2]/div[2]/div[1]/div/div[6]/div")
        next_form.click()
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div"
                                                      "/div/div[2]/div[2]/div[1]/div/div[3]/div/label/"
                                                      "div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        login = self.driver.find_element(By.XPATH,
                                         "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/"
                                         "div[2]/div[2]/div[2]/div/div/div")
        login.click()
        time.sleep(5)
        write_tweet = self.driver.find_element(By.XPATH,
                                               "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]"
                                               "/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div"
                                               "/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]"
                                               "/div/div/div/div")
        write_tweet.send_keys(
            f"Hey internet provider, why is my internet speed {self.down} down/{self.up} up when I "
            f"pay for 150 down/10 up?")
        time.sleep(2)
        send_tweet = self.driver.find_element(By.XPATH,
                                              "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div"
                                              "/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]"
                                              "/div[3]/div/span/span")
        send_tweet.click()
