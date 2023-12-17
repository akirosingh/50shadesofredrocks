import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import Keys
import time
import os

# Function to fetch data
# Function to fetch data
def fetch_data(driver, lat, lng, area_name, first_iteration):
    if first_iteration:
        url = f"https://shademap.app/@{lat},{lng},14z,1702444650890t,0b,0p,2m,qMzYuMTYxNjIsIC0xMTUuNDM1MDk=!{lat}!{lng}"
        driver.get(url)
    else:
        # Locate the search input and enter the new coordinates
        search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search..."]')
        search_input.clear()
        search_input.send_keys(f"{lat}, {lng}")
        search_input.send_keys(Keys.ENTER)  # Import Keys from selenium.webdriver.common.keys

    time.sleep(5)  # Wait for the page to update

    # Locate and click the download button
    download_button = driver.find_element(By.CSS_SELECTOR, 'a[title="Download"]')
    download_button.click()

    # Wait for download to complete (adjust time as needed)
    time.sleep(10)

    # Rename and move the downloaded file
    default_download_path = "C:\\Users\\17023\\Downloads"  # Update with your browser's download path
    downloaded_file = max([default_download_path + "\\" + f for f in os.listdir(default_download_path)], key=os.path.getctime)
    os.rename(downloaded_file, f"C:\\Users\\17023\\Desktop\\1-Projects\\50shadesofredrocks\\sunlight\\{area_name}.json")


driver = webdriver.Chrome(r"C:\Users\17023\Desktop\1-Projects\50shadesofredrocks\chromedriver.exe")  # Specify the correct path to your WebDriver

# Read CSV file
first_iteration = True
with open(r"C:\Users\17023\Desktop\1-Projects\50shadesofredrocks\redrockscrags.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lat, lng = row['coordinates'].split(',')
        fetch_data(driver, lat.strip(), lng.strip(), row['areas'], first_iteration)
        first_iteration = False  # Set to False after the first iteration

driver.quit()