from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load config
import json
with open("../config/config.json", "r") as file:
    config = json.load(file)

driver = webdriver.Chrome()
driver.get(config["url"])
time.sleep(2)

# Simulated message input
input_box = driver.find_element(By.NAME, "q")
for message in config["messages"]:
    input_box.clear()
    input_box.send_keys(message)
    input_box.send_keys(Keys.RETURN)
    print("Sent:", message)
    time.sleep(config["interval"])

driver.quit()
