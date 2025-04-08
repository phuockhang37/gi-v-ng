
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import cloudscraper
from bs4 import BeautifulSoup
import csv

url = 'https://www.investing.com/commodities/gold-historical-data' 

scraper = cloudscraper.create_scraper()

options = Options()

driver = Chrome(options=options) 

driver.get(url) 

# Check current URL
current_url = driver.current_url
print("Current URL:", current_url)

element = driver.find_element(By.XPATH, '//*[@class="historical-data-v2_selection-arrow__3mX7U relative flex flex-1 items-center justify-start gap-1 rounded border border-solid border-[#CFD4DA] bg-white bg-select-custom px-3 py-2 text-sm leading-5 text-[#333] shadow-select sm:w-[210px] "]')
element.click()

time.sleep(10);

element = driver.find_element(By.XPATH, '//*[@class="flex flex-1 flex-col justify-center text-sm leading-5 text-[#333]"]')
element.click()

time.sleep(60)  

soup = BeautifulSoup(driver.page_source, 'html.parser')
print("\n")

element = soup.find('table', class_='freeze-column-w-1 w-full overflow-x-auto text-xs leading-4')

with open('Gold_2003_2013.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['Date', 'Price', 'Open', 'High', 'Low', 'Vol', 'Change%'])
    
    for row in element.find_all('tr'):
        cells = row.find_all('td')
        if cells:
            date = cells[0].text.strip()
            price = cells[1].text.strip()
            open_price = cells[2].text.strip()
            high = cells[3].text.strip()
            low = cells[4].text.strip()
            vol = cells[5].text.strip()
            change_percent = cells[6].text.strip()

            writer.writerow([date, price, open_price, high, low, vol, change_percent])

print("Crawl thành công từ năm 1/1/2003 đến 31/12/2013")
