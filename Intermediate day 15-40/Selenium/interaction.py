from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pathlib
from time import sleep

DRIVER_PATH = f"{pathlib.Path(__file__).parent.absolute()}\\chromedriver.exe"
URL = "http://secure-retreat-92358.herokuapp.com/"

with Chrome(executable_path=DRIVER_PATH) as driver:
    driver.get(url=URL)

    fname = driver.find_element_by_name("fName")
    fname.send_keys("Denis")
    sleep(1)
    lname = driver.find_element_by_name("lName")
    lname.send_keys("Tu")
    sleep(1)
    email = driver.find_element_by_name("email")
    email.send_keys("DenisTu@mail.com")
    sleep(1)
    submit = driver.find_element_by_class_name("btn")
    sleep(1)
    submit.click()
    sleep(5)
