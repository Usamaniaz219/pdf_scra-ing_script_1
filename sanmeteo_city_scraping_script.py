from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import os
import json
from urllib.parse import urlparse

url = "https://law.cityofsanmateo.org/us/ca/cities/san-mateo/code/27"
parsed_url = urlparse(url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
print(base_url)

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
        id = h3.get_attribute("id")
        section_url = base_url+id
        section = {
            "heading": h3.text.strip(),
            "id": h3.get_attribute("id"),
            "url": section_url,
            "html": ""
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
 
        section["html"] = " ".join(paragraphs)
        print("Section HTML",section["html"])
        # results[chapter_title] = section
        if chapter_title not in results:
            # chapter_title = chapter_title.lower()
            results[chapter_title] = []
        results[chapter_title].append(section)
        # print("results type",results)
 

# for chapter_title, sections in results.items():
#     print(f"Chapter: {chapter_title}")
#     for sec in sections:
#         print(f" - {sec['heading']}")
#         print(f"{sec['html']}\n")


transform_structure_content = transform_structure(results)

with open("chapters.json", "w", encoding="utf-8") as f:
    json.dump(transform_structure_content, f, ensure_ascii=False, indent=4)


def extract_chapter_name(title):
    # This regex removes "Chapter <number>" (with optional dots or spaces) at the beginning
    return re.sub(r'^Chapter\s+\d+\.?\s*', '', title, flags=re.IGNORECASE).strip()

def normalize(text):
    return text.strip().rstrip('.').lower()


def chapters_wise_jsons(chapters,results):
    base_dir = "chapter_wise_jsons"
    os.makedirs(base_dir, exist_ok=True)

    # === Create files ===
    for i,chapter in enumerate(chapters):
        chapter_title = chapter["title"]
        chapter_title = extract_chapter_name(chapter_title)
        chapter_title = chapter_title.upper()
        chapter_title = normalize(chapter_title)

        chapter_title = next(
                    (key for key in results if normalize(key).endswith(chapter_title)),
                    None
                )

        
        chapter_dir = os.path.join(base_dir, chapter["dir"])
        os.makedirs(chapter_dir, exist_ok=True)

        if chapter_title not in results:
            print(f"Warning: No data for {chapter_title}")
            continue

        chapter_data = results[chapter_title]

    
        for section in chapter["sections"]:
            heading_clean = section["title"].replace("§", "").strip()
            # heading_clean = extract_chapter_name(heading_clean)
            # heading_clean = heading_clean.upper()

            # Match the heading from results
            match = next((item for item in chapter_data if heading_clean.endswith(item["heading"])), None)
            if not match:
                print(f"Warning: No match for section '{section['title']}'")
                continue

            section_data = {
                "source": "san-mateo",
                "title": section["title"],
                "url": match["url"],
                "html": f"{match['html']}"
            }

            filename = section["file"] + ".json"
            file_path = os.path.join(chapter_dir, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(section_data, f, indent=2, ensure_ascii=False)
    
    print(" Section files created successfully.")

chapters_wise_jsons(transform_structure_content,results)
driver.quit()
 