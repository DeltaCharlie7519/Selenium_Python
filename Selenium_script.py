from selenium import webdriver
import pandas as pd
import time


def scrape_data(metal,start_date,end_date,time_interval):

    driver = webdriver.Chrome('chromedriver')

    driver.get("https://www.investing.com/commodities/"+metal+"-historical-data")

    date_element = driver.find_element("xpath","//div[@class='DatePickerWrapper_icon__Qw9f8']")

    date_element.click()

    start_date_element = driver.find_element("xpath","//input[@value='2022-11-22']")

    start_date_element.click()

    start_date_element.clear()

    start_date_element.send_keys(start_date)

    time.sleep(5)

    apply_button_element = driver.find_element("xpath","//button[normalize-space()='Apply']")

    apply_button_element.click()

    time.sleep(5)

    download_data_element = driver.find_element("xpath","//span[@class='download-data_text__Myrn3']")

    download_data_element.click()

    time.sleep(60)

    data = pd.read_csv("C:/Users/Abhiram/Downloads/EUR_USD Historical Data.csv")

    return data

#calling the function
data = scrape_data("gold","12152015","12012022","Daily")
#printing the data
print(data)
