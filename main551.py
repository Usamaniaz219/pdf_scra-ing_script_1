from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from urllib.parse import urlparse
import re
import os
import csv
from utils import *

def transform_structure(data):
    output = []
    chapter_index = 1

    for chapter_title, sections in data.items():
        # Extract readable title
        match = re.match(r"Chapter\s+([\d.]+)\s+(.*)", chapter_title)
        readable_title = match.group(2).title() if match else chapter_title

        article = {
            "title": chapter_title,
            "dir": f"chapter_{chapter_index}",
            "file": "",
            "sections": []
        }

        for i, section in enumerate(sections, 1):
            section_entry = {
                "title": f"§ {section['heading']}",
                "file": f"{chapter_index}.{i}",
                "article": section.get("article", ""),  # Add article information
                "section": []
            }

            # Check for heading4 content
            if "h4_headings" in section and section["h4_headings"]:
                for j, h4_heading in enumerate(section["h4_headings"], 1):
                    section_entry["section"].append({
                        "subtitle": h4_heading,
                        "html": section.get("html", ""),
                        "text": section.get("text", "")
                    })
            else:
                section_entry["section"].append({
                    "html": section.get("html", ""),
                    "text": section.get("text", "")
                })

            article["sections"].append(section_entry)

        output.append(article)
        chapter_index += 1

    return output

def extract_chapter_name(title):
    return re.sub(r'^Chapter\s+\d+\.?\s*', '', title, flags=re.IGNORECASE).strip()

def normalize(text):
    return text.strip().rstrip('.').lower()

def chapters_wise_jsons(chapters, results):
    base_dir = "chapter_wise_jsons"
    os.makedirs(base_dir, exist_ok=True)

    for i, chapter in enumerate(chapters):
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

            match = next((item for item in chapter_data if heading_clean.endswith(item["heading"])), None)
            if not match:
                print(f"Warning: No match for section '{section['title']}'")
                continue

            section_data = {
                "source": "san-mateo",
                "title": section["title"],
                "article": section.get("article", ""),  # Include article in JSON
                "url": match["url"],
                "html": f"{match['html']}"
            }

            filename = section["file"] + ".json"
            file_path = os.path.join(chapter_dir, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(section_data, f, indent=2, ensure_ascii=False)
    
    print("Section files created successfully.")

def generate_csv(chapters, results, output_file="san_mateo_sections.csv"):
    rows = []
    max_chunk_length = 4000
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_length,
        chunk_overlap=0,
        separators=["\n\n", "\n", "(?<=\. )", " "]
    )

    for chapter_index, chapter in enumerate(chapters, 1):
        chapter_title_1 = chapter["title"]
        chapter_title = extract_chapter_name(chapter["title"])
        chapter_title_normalized = normalize(chapter_title)

        matched_chapter_key = next(
            (key for key in results if normalize(key).endswith(chapter_title_normalized)),
            None
        )

        if not matched_chapter_key or matched_chapter_key not in results:
            print(f"Warning: No data for chapter '{chapter_title}'")
            continue

        chapter_data = results[matched_chapter_key]

        for section_index, section in enumerate(chapter["sections"], 1):
            heading_clean = section["title"].replace("§", "").strip()
            section_url = section.get("url", "")

            match = next((item for item in chapter_data if heading_clean.endswith(item["heading"])), None)
            if not match or "text" not in match:
                print(f"Warning: No match for section '{section['title']}' in CSV export")
                continue

            subsection_number = f"{chapter_index}.{section_index}"
            zoneomics_url = f"https://zoneomics.com/code/san_mateo/chapter_{chapter_index}#{subsection_number}"

            text_content = match["text"]
            paragraphs = text_content.split("\n") if text_content else [""]

            for para in paragraphs:
                if not para.strip():
                    continue

                # para = municode_textProcessing(para)
                if len(para) > max_chunk_length:
                    split_texts = text_splitter.split_text(para)
                    for idx, split_text in enumerate(split_texts, 1):
                        row = {
                            "chapter_no": chapter_index,
                            "chapter_title": chapter_title_1,
                            "article_title": section.get("article", ""),  # New column for article
                            "section_title": match["heading"],
                            "subsection_number": f"sub-sec-{subsection_number}",
                            "source_url": match["url"],
                            "zoneomics_url": zoneomics_url,
                            "text": split_text.strip()
                        }
                        rows.append(row)
                else:
                    row = {
                        "chapter_no": chapter_index,
                        "chapter_title": chapter_title_1,
                        # "article_title": section.get("article", ""),  # New column for article
                        "article_title": match["article"],
                        "section_title": match["heading"],
                        "subsection_number": f"sub-sec-{subsection_number}",
                        "source_url": match["url"],
                        "zoneomics_url": zoneomics_url,
                        "text": para.strip()
                    }
                    rows.append(row)

    with open(output_file, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "chapter_no", "chapter_title", "article_title", "section_title",
            "subsection_number", "source_url", "zoneomics_url", "text"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV successfully written to {output_file}")

def scrape_sections(driver, chapter_number, base_url):
    sections = []
    
    
    print("chapter number",chapter_number)
    # First check for articles (h3 with class 'article-title')
    # articles = driver.find_elements(By.XPATH, f"//h3[contains(@class, 'article-title') and contains(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]")
  
    if chapter_number == "27.21":
        # pass
        article_path = "//h3[@class='h__article']"
        h3_articles = driver.find_elements(By.XPATH, article_path)

        # All h4 section elements (subsections) for this chapter
        h4_sections = driver.find_elements(By.XPATH,f"//*[contains(@class, 'h__section') and contains(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]" )

        i = 0  # global h4 index

        for h3 in h3_articles: 
            article_title = h3.text.strip()

            while i < len(h4_sections):
                h4 = h4_sections[i]
                section_id = h4.get_attribute("id")
                section_url = base_url + section_id

                section = {
                    "article": article_title,
                    "heading": h4.text.strip(),
                    "id": section_id,
                    "url": section_url,
                    "html": "",
                    "text": ""
                }

                paragraphs_html = []
                paragraphs_text = []

                try:
                    sibling = h4.find_element(By.XPATH, "following-sibling::*[1]")
                except:
                    i += 1
                    continue

                found_h3 = False
                break_outer_loop = False

                while True:
                    try:
                        tag = sibling.tag_name.lower()
                        cls = sibling.get_attribute("class")

                        if tag == 'p':
                            paragraphs_text.append(sibling.text.strip())
                            paragraphs_html.append(sibling.get_attribute('outerHTML'))
                            
                        elif tag == 'hr':
                            break_outer_loop = True
                            break # Only break the inner loop



                        elif tag == 'h3' and 'h__article' in cls:
                            found_h3 = True
                            break
                            # continue

                        elif tag == 'div' and 'table_wrap' in cls:
                            table_element = sibling.find_element(By.TAG_NAME, 'table')
                            markdown_text = table_to_markdown_with_chunks(table_element)
                            if markdown_text:
                                paragraphs_text.append(markdown_text)
                            paragraphs_html.append(sibling.get_attribute('outerHTML'))

                        sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")

                    except:
                        break

                # if break_outer_loop:
                #     section["text"] = "\n".join(paragraphs_text).strip()
                #     section["html"] = "\n".join(paragraphs_html).strip()
                #     if section["text"] or section["html"]:
                #         sections.append(section)

                #     i += 1  # Skip current h4 and continue with the next one
                #     continue

                # section["text"] = "\n".join(paragraphs_text).strip()
                # section["html"] = "\n".join(paragraphs_html).strip()
                # if section["text"] or section["html"]:
                #     sections.append(section)

                section["text"] = "\n".join(paragraphs_text)
                section["html"] = "\n".join(paragraphs_html)

                # Save or process section here
                sections.append(section)

                i += 1  # Proceed to next h4

                if i==8:
                    break  # Proceed to next h3 article



    if chapter_number in ['27.19', '27.28', '27.60', '27.62']:
        pass
        # article_path = f"//*[contains(@class, 'h__section') and contains(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]/preceding-sibling::h2[1]"
        # h3_articles = driver.find_elements(By.XPATH, article_path)

        # # All h4 section elements (subsections) for this chapter
        # h4_sections = driver.find_elements(By.XPATH, f"//*[contains(@class, 'h__section') and contains(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]")

        # i = 0  # global h4 index

        # for h3 in h3_articles:
        #     article_title = h3.text.strip()

        #     # Process h4s starting from where we left off
        #     while i < len(h4_sections):
        #         h4 = h4_sections[i]
        #         section_id = h4.get_attribute("id")
        #         section_url = base_url + section_id

        #         section = {
        #             "article": article_title,
        #             "heading": h4.text.strip(),
        #             "id": section_id,
        #             "url": section_url,
        #             "html": "",
        #             "text": ""
        #         }

        #         paragraphs_html = []
        #         paragraphs_text = []

        #         # Start looking at siblings of the h4
        #         try:
        #             sibling = h4.find_element(By.XPATH, "following-sibling::*[1]")
        #         except:
        #             i += 1
        #             continue

        #         found_h2 = False  # flag to exit current article loop
        #         #########################
        #         break_outer_loop = False
        #         ########################
        #         while True:
        #             try:
        #                 tag = sibling.tag_name.lower()

        #                 if tag == 'h2':
        #                     # New chapter marker – break only h4 loop, move to next h3
        #                     found_h2 = True
        #                     break

        #                 # elif tag == 'hr':
        #                 #     break_outer_loop = True
        #                 #     break  # Only break the inner loop

        #                 elif tag == 'h3':
        #                     # New article marker – break h4 loop, move to next h3
        #                     break

        #                 elif tag == 'p':
        #                     paragraphs_text.append(sibling.text.strip())
        #                     paragraphs_html.append(sibling.get_attribute('outerHTML'))

        #                 elif tag == 'div' and 'table_wrap' in sibling.get_attribute("class"):
        #                     table_element = sibling.find_element(By.TAG_NAME, 'table')
        #                     markdown_text = table_to_markdown_with_chunks(table_element)
        #                     if markdown_text:
        #                         paragraphs_text.append(markdown_text)
        #                     paragraphs_html.append(sibling.get_attribute('outerHTML'))

        #                 sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")

        #             except:
        #                 break


        #         section["text"] = "\n".join(paragraphs_text)
        #         section["html"] = "\n".join(paragraphs_html)

        #         # Save or process section here
        #         sections.append(section)

        #         i += 1  # next h4 section

        #         if found_h2:
        #             break  # stop processing further h4s for this h3, move to next h3



    else:
        pass
        
        # h3_elements = driver.find_elements(By.XPATH, f"//*[contains(@class, 'h__section') and contains(@id, '/us/ca/cities/san-mateo/code/{chapter_number}')]")
        # for i, h3 in enumerate(h3_elements, 1):
        #     id = h3.get_attribute("id")
        #     section_url = base_url + id
        #     section_index = 1
        #     # file_number = f"{title_count}.{i}"

        #     section = {
        #         "article": '',
        #         "heading": h3.text.strip(),
        #         "id": id,
        #         "url": section_url,
        #         # "file": file_number,
        #         "html": "",
        #         "text": ""
        #     }

        #     paragraphs_html = []
        #     paragraphs_text = []
        #     sibling = h3.find_element(By.XPATH, "following-sibling::*[1]")

        #     while sibling.tag_name not in ['h2', 'h3']:
        #         try:
        #             tag = sibling.tag_name.lower()
        #             cls = sibling.get_attribute("class")

        #             if tag == 'p':
        #                 paragraphs_text.append(sibling.text.strip())
        #                 paragraphs_html.append(sibling.get_attribute('outerHTML'))

        #             elif tag == 'div' and 'table_wrap' in cls:
        #                 # paragraphs_text.append(sibling.text.strip())
        #                 # paragraphs_html.append(sibling.get_attribute('outerHTML'))
        #                 table_element = sibling.find_element(By.TAG_NAME, 'table')  # <== This gives you the <table> Selenium WebElement
        #                 table_text = table_element.text
        #                 table_html = table_element.get_attribute("outerHTML")
        #                 print("table html",table_element.get_attribute("outerHTML"))
        #                 # Optionally, use your table processing function here
        #                 markdown_text = table_to_markdown_with_chunks(table_element)
        #                 if markdown_text:
        #                     paragraphs_text.append(markdown_text)

        #                 # Always append raw HTML as fallback
        #                 paragraphs_html.append(sibling.get_attribute('outerHTML'))

        #             # Move to the next sibling
        #             sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")

        #         except:
        #             break
        #     section["html"] = "\n".join(paragraphs_html)
        #     section["text"] = "\n".join(paragraphs_text)
        #     sections.append(section)
        
    
    return sections


# Main execution
url = "https://law.cityofsanmateo.org/us/ca/cities/san-mateo/code/27"
parsed_url = urlparse(url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

# Get all chapter links
chapter_links_xpath = "//div[@class='toc-menu']/ul/li/ul/li[27]/ul/li"
chapter_links = driver.find_elements(By.XPATH, chapter_links_xpath)
results = {}

for iter, chapter_link in enumerate(chapter_links, 1):
    chapter_link.click()
    time.sleep(2)
    
    chapter_title = chapter_link.text.strip()
    chapter_number = chapter_title.split()[1]
    
    chapter_title_xpath = f"//h2[@id='/us/ca/cities/san-mateo/code/{chapter_number}']"
    chapter_title_elements = driver.find_elements(By.XPATH, chapter_title_xpath)
    if chapter_title_elements:
        chapter_title = chapter_title_elements[0].text
    
    chapter_sections = scrape_sections(driver, chapter_number, base_url)
    results[chapter_title] = chapter_sections

# Transform and save results
transform_structure_content = transform_structure(results)

with open("chapters.json", "w", encoding="utf-8") as f:
    json.dump(transform_structure_content, f, ensure_ascii=False, indent=4)

chapters_wise_jsons(transform_structure_content, results)
generate_csv(transform_structure_content, results)

driver.quit()