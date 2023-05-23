from bs4 import BeautifulSoup as bs 
import requests as req 
import os
import constants as const
import time
from selenium import webdriver

search_term = ""
image_count = 100

def main():
    print("Enter the search term...\n")
    search_term = str(input())
    print()
    print("Enter the number images to scrap...\n")
    image_count = int(input())
    search_and_download()

def search_and_download():
    target_folder = os.path.join(const.TARGET_PATH, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with 















if __name__ == "__main__":
    print("This is a Google Image Scrapper made with python.")
    print()
    main()
