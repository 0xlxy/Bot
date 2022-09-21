from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--log-level=3")

# uncommect below line to use headless mode
options.headless = True

while True:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get("https://www.toutoupiao.com/VoteItem/428720")
    driver.find_element("id", "428720").click()
    while driver.find_element("id", "428720").text != "VOTED":
        sleep(0.5)
    driver.delete_all_cookies()
    driver.quit()
