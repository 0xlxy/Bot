from time import sleep

from joblib import Parallel, delayed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--log-level=3")
options.add_extension("uBlock-Origin.crx")


def main():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    # uncommect below line to use headless mode
    driver.set_window_position(-10000, 0)
    driver.get("https://www.toutoupiao.com/VoteItem/428720")
    while True:
        driver.find_element("id", "428720").click()
        while driver.find_element("id", "428720").text != "VOTED":
            sleep(0.5)
        driver.delete_all_cookies()
        driver.refresh()


Parallel(n_jobs=-1)(delayed(main)() for _ in range(20))