from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL = ''
ACCOUNT_PASSWORD = ''

chrome_driver_path = 'C:\\Users\\home\\Documents\\GitHub\\100-Days-of-code-PY\\Intermediate day ' \
                     '15-40\\Selenium\\chromedriver.exe '
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/")


time.sleep(5)
email_field = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(10)
jobs = driver.find_element_by_xpath('/html/body/div[8]/header/div[2]/nav/ul/li[3]')
jobs.click()

time.sleep(10)

job_title = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/section/section[1]/div/div[2]/div['
                                         '1]/div/div/div/input')
job_title.send_keys("python developer")
time.sleep(3)
job_location = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/section/section[1]/div/div[2]/div['
                                            '2]/div/div/div/input')
job_location.send_keys("Israel")
job_location.send_keys(Keys.ENTER)
time.sleep(5)

easy_apply = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div[3]/section/div/div/div/div[1]/div/div['
                                          '2]/ul/li[8]/div')
easy_apply.click()

time.sleep(5)
driver.close()
#TODO end this project
