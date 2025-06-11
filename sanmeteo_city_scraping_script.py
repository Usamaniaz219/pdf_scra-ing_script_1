from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

import json




def transform_structure(data):
    output = []
    chapter_index = 1

    for chapter_title, sections in data.items():
        # Extract readable title
        match = re.match(r"Chapter\s+([\d.]+)\s+(.*)", chapter_title)
        # chapter_code = match.group(1) if match else f"{chapter_index:02d}"
        readable_title = match.group(2).title() if match else chapter_title

        article = {
            "title": f"Chapter {str(chapter_index)} {readable_title}",
            "dir": f"chapter_{chapter_index}",
            "file": "",
            "sections": []
        }

        for i, section in enumerate(sections, 1):
            section_entry = {
                "title": f"§ {section['heading']}",
                "file": f"{chapter_index}.{i}",
                "section": []
            }
            article["sections"].append(section_entry)

        output.append(article)
        chapter_index += 1

    return output
 
# Set up your WebDriver (example: Chrome)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH
driver.get("https://law.cityofsanmateo.org/us/ca/cities/san-mateo/code/27")  # Replace with the actual page URL
 
chapter_links_xpath = "//div[@class='toc-menu']/ul/li/ul/li[27]/ul/li"
 
chapter_links = driver.find_elements(By.XPATH, chapter_links_xpath)
results = {}
 
for chapter_link in chapter_links:
    
    chapter_link.click()

    chapter_title_1 = chapter_link.text.strip()
    extracting_number = chapter_title_1.split()
    chapter_number = extracting_number[1]
    time.sleep(3)
 
    chapter_title_xpath = f"//h2[@id='/us/ca/cities/san-mateo/code/{chapter_number}']"
    chapter_title_element = driver.find_elements(By.XPATH, chapter_title_xpath)
 
    if chapter_title_element:
        chapter_title = chapter_title_element[0].text
 
    # Find all <h3> elements matching the zoning code ID pattern
    h3_elements = driver.find_elements(By.XPATH, f"//h3[starts-with(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]")
 
    
 
    for h3 in h3_elements:
        section = {
            "heading": h3.text.strip(),
            "id": h3.get_attribute("id"),
            "text": ""
        }
        paragraphs = []
        # Start walking through the siblings
        sibling = h3.find_element(By.XPATH, "following-sibling::*[1]")
        
        while sibling.tag_name not in ['h2', 'h3']:
            if sibling.tag_name == 'p':
                # outer_html = sibling.get_attribute('outerHTML')
                # paragraphs.append(sibling.text.strip())
                paragraphs.append(sibling.get_attribute('outerHTML'))
            try:
                sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")
            except:
                break
 
        section["text"] = " ".join(paragraphs)
        # results[chapter_title] = section
        if chapter_title not in results:
            results[chapter_title] = []
        results[chapter_title].append(section)
        # print("results type",results)
 

for chapter_title, sections in results.items():
    print(f"Chapter: {chapter_title}")
    for sec in sections:
        print(f" - {sec['heading']}")
        print(f"{sec['text']}\n")




transform_structure_content = transform_structure(results)


with open("san_mateo_code_results_11.json", "w", encoding="utf-8") as f:
    json.dump(transform_structure_content, f, ensure_ascii=False, indent=4)
 
driver.quit()
 