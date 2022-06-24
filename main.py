from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
from pystyle import *
import time
import random
import string
import requests

os.system('title 0xRedditFucker ^| By KynZay#4521 ^| using : Reddit Creator')

def __init__(self, profile, proxy = None):
    self.session = requests.Session()
    self.profile = profile
    self.proxy = proxy

print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " starting up..")
driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
password = ("0xBotterEveryware")
usr = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " loaded !")

def register_account(self):
    proxies = None
    if self.proxy != None:
        proxies = {"https": f"http://{self.proxy}"}

driver.get("https://www.reddit.com/register/")
time.sleep(5)
driver.find_element_by_id("regEmail").clear
time.sleep(0.5)
driver.find_element_by_id("regEmail").send_keys(email)
time.sleep(0.5)
driver.find_element_by_xpath("""/html/body/div/main/div[1]/div/div[2]/form/fieldset[3]/button""").click()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="regUsername"]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="regUsername"]""").send_keys(usr)
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="regPassword"]""").clear()
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="regPassword"]""").send_keys(password)
print(Colors.red + "PLEASE RESOLVE CAPTCHA !!")
time.sleep(15)
driver.find_element_by_xpath("""/html/body/div/main/div[2]/div/div/div[3]/button""").click()

with open("Created.txt", "a") as f:
    f.read(f'{email}:{password}:{usr}\n')