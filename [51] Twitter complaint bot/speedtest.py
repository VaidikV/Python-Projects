import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\\Development\\chromedriver.exe"
s = Service(path)


class Speedtest:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.driver.quit()
