from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("enable-automation")

driver = webdriver.Chrome(options=options)
driver.get("https://socialblade.com/youtube/c/bitpin")

time.sleep(10)

element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[1]/p[2]')  # your XPath here
print("Found:", element.text)
driver.quit()
