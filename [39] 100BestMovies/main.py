"""
This is not the way this web scraping had to be done. I have just completed this code for the sake of completing it.
This website changed to using restapi which resulted in h3 tag not showing up in the soup. So hopefully in the
next session I will learn how to scrape this website with better tools and complete this project the way it was
meant to be completed.
"""

import requests
from selenium import webdriver
from
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movies_tag = soup.find_all(name="div", class_="jsx-3523802742 listicle-item")

movies = [movie.find(name="img")["alt"] for movie in movies_tag]
movies.reverse()
with open("100BestMovies.txt", mode="w", encoding="utf-8") as file:
    index = 1
    for movie in movies:
        file.write(f"{index}) {movie}\n")
        index += 1



