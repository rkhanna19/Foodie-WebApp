#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from pprint import pprint

class ImageBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        sleep(2)

    def find_image(self, food_name):
        search_box = self.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        search_box.send_keys(food_name, Keys.ENTER)
        self.driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div/div[2]/a").click()
        source = self.driver.page_source
        image_url = self.find_image_helper(source)
        return image_url
    
    def find_image_helper(self, page):
        image_url = ""
        image_types = ["jpg", "png", "gif", "pdf", "eps", "ai"]
        for image_type in image_types:
            index = page.find("." + image_type)
            if index != -1:
                image_url += image_type
                while page[index] != "\"":
                    image_url = page[index] + image_url
                    index -= 1
                break
            else: continue
        return image_url

    def reset(self):
        self.driver.back()
        self.driver.back()

    def kill(self):
        self.driver.close()

# bot = ImageBot()
# image_url = bot.find_image("Gobhi masala")
# print(image_url)
# sleep(5)
# bot.reset()
# bot.kill()