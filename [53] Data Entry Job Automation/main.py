import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


headers = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664."
                  "110 Safari/537.36",
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D"
                        "%2C%22mapBounds%22%3A%7B%22west%22%3A-122.4673957497283%2C%22east%22%3A-122.32182690207205%2"
                        "C%22south%22%3A37.78778584256872%2C%22north%22%3A37.82630367043599%7D%2C%22mapZoom%22%3A13%2C"
                        "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%"
                        "22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22m"
                        "ax%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7"
                        "D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22"
                        "%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%"
                        "22%3Atrue%7D", headers=headers)

# TODO 1: Scrape all listings from zillow.
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, "html.parser")

# Scraping the webpage to get links, prices and addresses respectively.
links = [listing.get("href") for listing in soup.find_all(name="a", class_="list-card-link")]
print(len(links[0:9]))

prices = [listing.getText().strip("/mo").split("+")[0] for listing in
          soup.find_all(name="div", class_="list-card-price")]
print(len(prices))

addresses = [listing.getText() for listing in soup.find_all(name="address", class_="list-card-addr")]
print(len(addresses))

# TODO 2: Use selenium to fill the google form
driver = webdriver.Chrome(executable_path="C:\\Development\\chromedriver.exe")

for number in range(9):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeU-a5cHx_cap2W6WIy43F9xgv97EyCqUwcMDn6w28_Sd5gIA/viewform")

    address_space = driver.find_element(By.XPATH,
                                        "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/"
                                        "div/div[1]/input")

    price_space = driver.find_element(By.XPATH,
                                      "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/d"
                                      "iv/div[1]/input")

    link_space = driver.find_element(By.XPATH,
                                     "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div"
                                     "/div[1]/input")
    time.sleep(1)
    address_space.send_keys(addresses[number])
    price_space.send_keys(prices[number])
    link_space.send_keys(links[number])
    submit_button = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

# For now, this works. But there are only 9 results. It has something to do with the page returning JSON object.
# Go to this url- https://www.udemy.com/course/100-days-of-code/learn/lecture/21866762#questions/15149028
# and look at the answer by Marceia. They explain how they tackled this problem, but I feel that it is a bit too
# advanced




