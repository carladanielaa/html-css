from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time import sleep
import intaloader
import random
import os.path

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path="C:\Users\julio\OneDrive\Área de Trabalho\fgdhd\geckodriver-v0.31.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

jhonatanBot = InstagramBot('IssoVaiDominarOMundo','aindaBemQueEuSeiCriarUm')
jhonatanBot.login()        

