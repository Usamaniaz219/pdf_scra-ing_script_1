from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import os
import json
from urllib.parse import urlparse
import csv
import html
from markdownify import markdownify as md
import math
# from utils.text_processing import *
from collections import Counter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from text_processing import *

url = "https://law.cityofsanmateo.org/us/ca/cities/san-mateo/code/27"
parsed_url = urlparse(url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
print(base_url)



###########################################################################



# ------------------------------------Duplicate Section Start----------------------------------------------------------------

def get_repeated_table_elements(table_elements: list):

    if not table_elements:
        return []
    repeated_tables = []
    i = 0
    while i < len(table_elements) - 1:
        current_text = table_elements[i].text.strip()
        next_text = table_elements[i + 1].text.strip()
        if current_text and current_text in next_text:
            repeated_tables.append(table_elements[i])
            i += 1  
        else:
            i += 1

    return repeated_tables


# def get_common_headings_in_repeated_tables(repeated_tables: list):
def get_shared_headings(repeated_tables: list):

    table_texts = []
    for table in repeated_tables:
        table_texts.append(table.text)
    table_duplicates = [item for item, count in Counter(table_texts).items() if count > 1]
    if len(table_duplicates) > 0:
        return table_duplicates
    else:
        return None


def remove_repeated_tables(table_elements):
    
    if not table_elements:
        return []
    filtered_tables = []
    i = 0
    while i < len(table_elements) - 1:
        current_text = table_elements[i].text.strip()
        next_text = table_elements[i + 1].text.strip()
        if current_text and current_text in next_text:
            i += 1  
        else:
            filtered_tables.append(table_elements[i])
            i += 1
    if i == len(table_elements) - 1:
        filtered_tables.append(table_elements[-1])

    return filtered_tables


def replace_second_occurrence(text, sub, replacement=""):

    first_index = text.find(sub)
    if first_index == -1:
        return text  # not found at all
    second_index = text.find(sub, first_index + len(sub))
    if second_index == -1:
        return text  # only one occurrence
    
    return text[:second_index] + replacement + text[second_index + len(sub):]


def remove_repeated_tables_text(page_text, duplicate_tables):

    duplicate_headers = get_shared_headings(duplicate_tables)
    duplicate_flag = False
    if duplicate_headers:
        for table in duplicate_tables:
            table_text = table.text
            if table_text not in duplicate_headers:
                if table_text in page_text:
                    page_text = page_text.replace(table_text, "", 1)
                else:
                    print("Table Text Not Found For Duplicate Table")
            else:
                if duplicate_flag == False:
                    if table_text in page_text:
                        page_text = page_text.replace(table_text,"",1)
                        duplicate_flag = True
                    else:
                        print("Table Text Not Found For Duplicate Table")
        for table_text in duplicate_headers:
            page_text = replace_second_occurrence(page_text, table_text)
        return page_text
    else:
        for table in duplicate_tables:
            table_text = table.text
            if table_text in page_text:
                page_text = page_text.replace(table_text, "", 1)
            else:
                print("Table Text Not Found For Duplicate Table")
        return page_text


# ------------------------------------------------- Duplicate Section End ----------------------------------------------------



# ---------------------------------------------- Large Tables Splitting Pipeline --------------------------------------------


def get_large_tables_markdowns(table_elements):

    large_tables_dict = {}

    for index, table_element in enumerate(table_elements):

        table_html = table_element.get_attribute("outerHTML")
        table_markdown = md(table_html, heading_style="ATX", strip = ["a"])
        if len(table_markdown) > 6000:
            large_tables_dict[index] = table_markdown

    return large_tables_dict


def get_top_three_lines(table_markdown):

    def has_min_alphanum(line, min_count=3):
        alnum_count = sum(char.isalnum() for char in line)
        return alnum_count >= min_count
    
    top_three_lines = []
    table_md_lines = table_markdown.split("\n")
    count = 0
    for line in table_md_lines[:6]:
        if count >=3:
            break

        if has_min_alphanum(line):
            top_three_lines.append(line)
            count = count + 1
    
    top_three_lines = "\n".join(top_three_lines)
    return top_three_lines



def update_large_table_markdown(large_table_markdwon):

    full_table_markdown = ""
    start_phrase = "\nTABLE STARTS HERE\n"
    end_phrase = "\nTABLE ENDS HERE\n"
    table_md_length = len(large_table_markdwon)
    chunk_size = 4000
    num_splits = math.ceil(table_md_length / chunk_size)
    large_table_markdwon_lines = large_table_markdwon.split("\n")
    lines_in_table_md = len(large_table_markdwon_lines)
    top_three_lines = get_top_three_lines(large_table_markdwon)
    lines_per_md = lines_in_table_md // num_splits
    remainder_lines = lines_in_table_md % num_splits
    start_idx = 0
    for i in range(num_splits):
        end_idx  = start_idx + lines_per_md + (1 if i < remainder_lines else 0)
        splitted_md = large_table_markdwon_lines[start_idx: end_idx]
        splitted_md = " \n".join(splitted_md)
        if i !=0:
            splitted_md = f"{top_three_lines}\n{splitted_md}"
        full_table_markdown = full_table_markdown + f"{start_phrase}{splitted_md}{end_phrase}"
        start_idx = end_idx
    if end_idx != lines_in_table_md:
        print("Some Data is Missed!")
        return None

    return full_table_markdown


def update_original_markdowns_list(large_tables_markdowns, all_markdowns):

    for index, table_markdown in large_tables_markdowns.items():
        updated_markdown = update_large_table_markdown(table_markdown)
        if updated_markdown == None:
            return None
        all_markdowns[index] = updated_markdown
    
    return all_markdowns


def large_tables_pipeline(table_elements):

    large_tables_dict = get_large_tables_markdowns(table_elements)
    all_markdowns = convert_table_text_to_markdown(table_elements)
    updated_markdowns = update_original_markdowns_list(large_tables_dict, all_markdowns)
    if updated_markdowns == None:
        print("Error in large tables pipeline")
        return None
    return updated_markdowns


# ---------------------------------------------------------Large Tables Pipeline End --------------------------------------------------------


# ---------------------------------------------------------Table to Markdown Pipeline Start -------------------------------------------------

# def detect_table_in_element(element):

#     table_elements = element.find_elements(By.TAG_NAME, "table")
#     if table_elements:
#         valid_tables = []
#         for table_element in table_elements:
#             table_text = table_element.text
#             if table_text != "":
#                 valid_tables.append(table_element)
#         if len(valid_tables) > 1:
#             unique_tables = remove_repeated_tables(valid_tables)
#             return unique_tables, valid_tables
#         else:
#             return valid_tables, valid_tables
#     else:
#         return None, None
    

def detect_table_in_element(element):

    # table_elements = element.find_elements(By.TAG_NAME, "table")
    # if table_elements:
    valid_tables = []
    # for table_element in table_elements:
    table_text = element.text
        # if table_text != "":
    if table_text:
        valid_tables.append(element)
        if len(valid_tables) > 1:
            unique_tables = remove_repeated_tables(valid_tables)
            return unique_tables, valid_tables
        else:
            return valid_tables, valid_tables
    # else:
        # return None, None


    

def extract_table_text(table_elements):

    all_table_elements_text = []
    for table_element in table_elements:
        table_text = table_element.text
        if table_text != "":
            all_table_elements_text.append(table_text)
    
    return all_table_elements_text


def convert_table_text_to_markdown(table_elements):

    all_table_markdowns = []
    start_phrase = "\nTABLE STARTS HERE\n"
    end_phrase = "\nTABLE ENDS HERE\n"

    for table_element in table_elements:
        table_html = table_element.get_attribute("outerHTML")
        table_markdown = md(table_html, heading_style="ATX", strip = ["a"])
        table_markdown_updated = f"{start_phrase}{table_markdown}{end_phrase}"
        all_table_markdowns.append(table_markdown_updated)

    return all_table_markdowns


def replace_table_text_with_dummy_text(page_data, all_tables_text):

    unique_token = "UniQuE_TaBLe_TokEn_TO_bEE_RepLAcEd_LaTEr"
    for table_text in all_tables_text:
        if table_text in page_data:
            page_data = re.sub(re.escape(table_text), unique_token, page_data, count=1)
        else:
            print("Table_Text Not Found!")

    return page_data


def modify_tables_text(table_markdowns, page_data):

    unique_token = "UniQuE_TaBLe_TokEn_TO_bEE_RepLAcEd_LaTEr"
    for i in range(len(table_markdowns)):

        tables_markdown = table_markdowns[i]
        page_data = re.sub(re.escape(unique_token), lambda match: tables_markdown, page_data, count=1)

    return page_data


def table_to_markdown_with_chunks(element, output_type = None):

    valid_tables, all_tables = detect_table_in_element(element)
    element_text = element.text
    if valid_tables:
        tables_markdowns = convert_table_text_to_markdown(valid_tables)
        large_tables = get_large_tables_markdowns(valid_tables)
    
        if large_tables:
            tables_markdowns_updated = large_tables_pipeline(valid_tables)
            if tables_markdowns_updated == None:
                print(f"Some Error Processing Large Tables")
                return None
            else:
                tables_markdowns = tables_markdowns_updated
                
        duplicate_tables = get_repeated_table_elements(all_tables)
        if duplicate_tables:
            element_text = remove_repeated_tables_text(element_text, duplicate_tables)

        tables_text = extract_table_text(valid_tables)
        element_dummy_text = replace_table_text_with_dummy_text(element_text, tables_text)
        # if source == "ecode":
        #     processed_text = ecode_textProcessing(element_dummy_text, output_type)
        # elif source == "municode":
        #     processed_text = municode_textProcessing(element_dummy_text)
        # elif source == "amlegal":
        #     processed_text = amlegal_textProcessing(element_dummy_text)

        element_text = modify_tables_text(tables_markdowns, element_dummy_text)
        return element_text
    else:
        element_text = element.text
        # if source == "ecode":
        #     element_text = ecode_textProcessing(element_text, output_type)
        # elif source == "municode":
        #     element_text = municode_textProcessing(element_text)
        return element_text


# def table_to_markdown_without_chunks(element):

#     valid_tables, all_tables = detect_table_in_element(element)
#     element_text = element.text
#     if valid_tables:
#         tables_markdowns = convert_table_text_to_markdown(valid_tables)
#         duplicate_tables = get_repeated_table_elements(all_tables)
#         if duplicate_tables:
#             element_text = remove_repeated_tables_text(element_text, duplicate_tables)
#         tables_text = extract_table_text(valid_tables)
#         element_dummy_text = replace_table_text_with_dummy_text(element_text, tables_text)
#         processed_text = textProcessing(element_dummy_text)
#         element_text = modify_tables_text(tables_markdowns, processed_text)
#         return element_text
#     else:
#         element_text = element.text
#         element_text = textProcessing(element_text)
#         return element_text
# ---------------------------------------------------- Table To Markdown Pipeline End --------------------------------------------------------









####################################################################################
#####################################################################################

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
 
for iter, chapter_link in enumerate(chapter_links):
    title_count = iter + 1
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
 
    for i, h3 in enumerate(h3_elements, 1):
        id = h3.get_attribute("id")
        section_url = base_url + id
        section_index = 1
        file_number = f"{title_count}.{i}"

        section = {
            "heading": h3.text.strip(),
            "id": id,
            "url": section_url,
            "file": file_number,
            "html": "",
            "text": ""
        }

        paragraphs_html = []
        paragraphs_text = []
        sibling = h3.find_element(By.XPATH, "following-sibling::*[1]")

        # while sibling.tag_name not in ['h2', 'h3']:
        #     if sibling.tag_name == 'p':
        #         paragraphs_text.append(sibling.text.strip())
        #         paragraphs_html.append(sibling.get_attribute('outerHTML'))
        #     try:
        #         sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")
        #     except:
        #         break

        while sibling.tag_name not in ['h2', 'h3']:
            try:
                tag = sibling.tag_name.lower()
                cls = sibling.get_attribute("class")

                if tag == 'p':
                    paragraphs_text.append(sibling.text.strip())
                    paragraphs_html.append(sibling.get_attribute('outerHTML'))

                elif tag == 'div' and 'table_wrap' in cls:
                    # paragraphs_text.append(sibling.text.strip())
                    # paragraphs_html.append(sibling.get_attribute('outerHTML'))
                    table_element = sibling.find_element(By.TAG_NAME, 'table')  # <== This gives you the <table> Selenium WebElement
                    table_text = table_element.text
                    table_html = table_element.get_attribute("outerHTML")
                    print("table html",table_element.get_attribute("outerHTML"))
                    # Optionally, use your table processing function here
                    markdown_text = table_to_markdown_with_chunks(table_element)
                    if markdown_text:
                        paragraphs_text.append(markdown_text)

                    # Always append raw HTML as fallback
                    paragraphs_html.append(sibling.get_attribute('outerHTML'))

                # elif tag in ['ul', 'ol', 'table']:
                #     paragraphs_text.append(sibling.text.strip())
                #     paragraphs_html.append(sibling.get_attribute('outerHTML'))

                # Move to the next sibling
                sibling = sibling.find_element(By.XPATH, "following-sibling::*[1]")

            except:
                break

        section["html"] = f"<div id='{file_number}'>{' '.join(paragraphs_html)}</div>"
        section["text"] = " ".join(paragraphs_text)

        ###########################################################
        
        # safe_id = html.escape(, quote=True)


        ################################################################

        # section["html"]= f"<div>{section['html']}</div>"
        
        # print("Section HTML",section_html_1)
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

with open("chapters_11.json", "w", encoding="utf-8") as f:
    json.dump(transform_structure_content, f, ensure_ascii=False, indent=4)


def extract_chapter_name(title):
    # This regex removes "Chapter <number>" (with optional dots or spaces) at the beginning
    return re.sub(r'^Chapter\s+\d+\.?\s*', '', title, flags=re.IGNORECASE).strip()

def normalize(text):
    return text.strip().rstrip('.').lower()


def chapters_wise_jsons(chapters,results):
    base_dir = "chapter_wise_jsons_55"
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



def generate_csv(chapters, results, output_file="san_mateo_sections_66.csv"):
    rows = []

    max_chunk_length = 4000
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_length,
        chunk_overlap=0,
        separators=["\n\n", "\n", "(?<=\. )", " "]
    )

    for chapter_index, chapter in enumerate(chapters, 1):
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

                para = municode_textProcessing(para)
                if len(para) > max_chunk_length:
                    split_texts = text_splitter.split_text(para)
                    for idx, split_text in enumerate(split_texts, 1):
                        row = {
                            "chapter_no": chapter_index,
                            "heading_1": chapter_title,
                            "heading_2": match["heading"],
                            # "subsection_number": f"sub-sec-{subsection_number}-{idx}",
                            "subsection_number": f"sub-sec-{subsection_number}",
                            "source_url": match["url"],
                            "zoneomics_url": zoneomics_url,
                            "text": split_text.strip()
                        }
                        rows.append(row)
                else:
                    row = {
                        "chapter_no": chapter_index,
                        "heading_1": chapter_title,
                        "heading_2": match["heading"],
                        "subsection_number": f"sub-sec-{subsection_number}",
                        "source_url": match["url"],
                        "zoneomics_url": zoneomics_url,
                        "text": para.strip()
                    }
                    rows.append(row)

    # Write to CSV
    with open(output_file, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "chapter_no", "heading_1", "heading_2",
            "subsection_number", "source_url", "zoneomics_url", "text"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV successfully written to {output_file}")



chapters_wise_jsons(transform_structure_content,results)
generate_csv(transform_structure_content, results)
driver.quit()
 