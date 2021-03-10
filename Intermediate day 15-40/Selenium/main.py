from selenium.webdriver import Chrome
from time import sleep
import pathlib


# driver_path = f"{pathlib.Path(__file__).parent.absolute()}\\chromedriver.exe"
# url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
#
#
# with Chrome(executable_path=driver_path) as driver:
#     driver.get(url=url)
#     sleep(2)
#     name = driver.find_element_by_id("productTitle")
#     rating = driver.find_element_by_css_selector("span.a-icon-alt").get_attribute('innerHTML')
#     price = driver.find_element_by_id("priceblock_ourprice")
#     print(f"Product: {name.text}\nRating: {rating}\nPrice: ${price.text}")

driver_path = f"{pathlib.Path(__file__).parent.absolute()}\\chromedriver.exe"
url = "https://www.python.org/"


with Chrome(executable_path=driver_path) as driver:
    driver.get(url=url)
    sleep(2)
    dates = driver.find_elements_by_css_selector(".event-widget time")
    names = driver.find_elements_by_css_selector(".event-widget li a")

    events = {}

    for n in range(len(dates)):
        events[n] = {
            "time": dates[n].text,
            "names": names[n].text
        }
    print(events)
