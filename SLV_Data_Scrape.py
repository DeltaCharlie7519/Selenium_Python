from selenium import webdriver
import pandas as pd
import time


def scrape_data(url,start_date,end_date,time_interval):

    driver = webdriver.Chrome('chromedriver')

    driver.get(url)

    download_data_element = driver.find_element("xpath","//a[normalize-space()='Download Data']")

    download_data_element.click()

    email_element = driver.find_element("xpath","//input[@id='loginFormUser_email']")

    email_element.click()

    email_element.clear()

    email_element.send_keys('sharmaabhiram1809@gmail.com')

    password_element = driver.find_element("xpath","//input[@id='loginForm_password']")

    password_element.click()

    password_element.clear()

    password_element.send_keys('GC6J285caS!ArUt')

    sign_in_element = driver.find_element("xpath","//a[@class='newButton orange']")

    sign_in_element.click()

    time.sleep(20)

    date_element = driver.find_element("xpath","//div[@id='flatDatePickerCanvasHol']//span[@class='datePickerIcon']")

    date_element.click()

    start_date_element = driver.find_element("xpath","//input[@id='startDate']")

    start_date_element.click()

    start_date_element.clear()

    start_date_element.send_keys(start_date)

    time.sleep(5)

    apply_button_element = driver.find_element("xpath","//a[@id='applyBtn']")

    apply_button_element.click()

    time.sleep(10)

    download_data_element = driver.find_element("xpath","//a[normalize-space()='Download Data']")

    download_data_element.click()

    time.sleep(60)

    return 0

#calling the function
data = scrape_data("https://www.investing.com/etfs/ishares-silver-trust-historical-data","01/15/2015","12012022","Daily")
#printing the data
print(data)