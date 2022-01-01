from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json

chromeDriverPath = '/home/dell/chromedriver_linux64/chromedriver'

service = Service(chromeDriverPath)
options = webdriver.ChromeOptions()
options.add_argument("--use--fake-ui-for-media-stream")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://mycurrentlocation.net/")
driver.minimize_window()

latitude = driver.find_element(By.ID,'latitude').text
longitude = driver.find_element(By.ID,'longitude').text
region = driver.find_element(By.ID,'regionname').text
neighborhood = driver.find_element(By.ID,'neighborhood').text

driver.quit()

address = neighborhood + ', '+ region

locationData = {}

locationData['latitude'] = latitude
locationData['longitude'] = longitude
locationData['address'] = address
with open('location.json', 'w') as outfile:
    json.dump(locationData, outfile)
    print('Location saved')