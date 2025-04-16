from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_elements_data(url, element_xpath, data_xpath="./text()", scroll=True, scroll_pause=2):
    """
    Generalized web scraper using Selenium.

    Parameters:
        url (str): The URL to scrape.
        element_xpath (str): XPath to locate each element to extract data from.
        data_xpath (str): Relative XPath from the element to extract specific data (text or attribute).
        scroll (bool): Whether to scroll the page to load more content.
        scroll_pause (int): Time (in seconds) to pause between scrolls.

    Returns:
        List[dict]: Extracted data in dictionary format.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        print(f"🔄 Fetching data from: {url}")
        driver.get(url)
        time.sleep(5)

        if scroll:
            body = driver.find_element(By.TAG_NAME, "body")
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                body.send_keys(Keys.END)
                time.sleep(scroll_pause)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

        elements = driver.find_elements(By.XPATH, element_xpath)
        items = []

        for elem in elements:
            try:
                if data_xpath == "./text()":
                    value = elem.text.strip()
                else:
                    sub_elem = elem.find_element(By.XPATH, data_xpath)
                    value = sub_elem.text.strip()
                if value:
                    items.append({"Data": value})
            except Exception as inner_e:
                print(f"Skipping element due to error: {inner_e}")
                continue

        return items

    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return []

    finally:
        driver.quit()
