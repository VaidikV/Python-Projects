from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib

our_dealprice = 4200
MY_EMAIL = "email"
MY_PASSWORD = "pass"
LINK = "https://www.amazon.in/Zebronics-Zeb-Glide-Multimedia-Keyboard-Connector/dp/B098JXNVVK/"

s = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(LINK)

price = int(driver.find_element(By.ID, "priceblock_dealprice").text.split(".")[0].strip("₹"))
print(price)
product_title = driver.find_element(By.ID, "productTitle").text

if price < our_dealprice:
    print("sending email")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Low price alert! Grab the amazon product now!\n\nYour product \"{product_title}\" is now"
                f" ₹{price}. "
                f"Here is the link to your product:\n{LINK}".encode()
        )
else:
    print("The price is not lower that what you want. Please check back later...")

driver.quit()


