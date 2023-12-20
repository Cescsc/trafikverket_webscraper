from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def main():
    opts = Options()
    # opts.add_argument("--headless=new")
    # opts.add_experimental_option("detach", True)

    browser = Chrome(options=opts)
    browser.implicitly_wait(5)
    browser.get('https://fp.trafikverket.se/Boka/#/search/AmaaMaOMeCTAtA/5/0/0/0')
    # html = browser.page_source
    # print(html)

    # browser.find_element(By.XPATH, '//select[contains(@data-bind,"click:selectExaminationType")]')
    # testtype = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-block.text-left')
    testtype = Select(browser.find_element(By.ID, 'examination-type-select'))
    testtype.select_by_visible_text("Körprov")

    vehicletype = Select(browser.find_element(By.ID, "vehicle-select"))
    vehicletype.select_by_visible_text("Automatbil")

    location = browser.find_element(By.ID, "id-control-searchText-1-1")
    location.send_keys("Sollentuna")
    location.send_keys(Keys.ENTER)

    try:
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block").click()
        print("Time found!")
        browser.quit()
        return 1

    except:
        print("No time found :(")
        time.sleep(30)
        browser.quit()
        return 0
