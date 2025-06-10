from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import time 
import json


#Initialize the Webdriver
driver = webdriver.Chrome()

#Wait
wait = WebDriverWait(driver,10)

driver.get("https://law.cityofsanmateo.org/us/ca/cities/san-mateo/code/27")
time.sleep(3)

all_chapters_headings = driver.find_elements(By.XPATH,'//span[contains(normalize-space(.),"Chapter")]')
# all_chapters_headings = driver.find_elements(By.XPATH,'//h2[@class="h__chapter"]')
# print(len(all_chapters_headings))
hierarchical_content = defaultdict(dict)

links = []
for chapter_heading in all_chapters_headings:
    chapter_link = chapter_heading.find_element(By.XPATH, './ancestor::a[1]')
   
    chapter_title = chapter_link.text.strip()
    chapter_link.click()
    # href = chapter_link.get_attribute("href")
    extracting_number = chapter_title.split()
    extracting_number = extracting_number[1]
    # extracting_number_concat = extracting_number+"."
    sub_headings = chapter_link.find_elements(By.XPATH,f'//span[contains(normalize-space(.),{extracting_number})]')
    print(type(sub_headings))
    for i,sub_heading in enumerate(sub_headings):
        if i==0:
            pass
        else:
            sub_heading_title = sub_heading.text.strip()
            sub_heading.click()
        # content_element = driver.find_elements(By.XPATH,"//p/text()[contains(., '"')])


   
    
    # if href:
        # links.append(href)

# for i,chapter_link in enumerate(links):
#     print(chapter_link)
#     driver.get(chapter_link)
#     time.sleep(3)
#     sub_sections = driver.find_elements(By.XPATH, '')
