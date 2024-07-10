import os
import time
import shutil
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

# Create main directory for downloaded PDFs
main_download_dir = "downloaded_pdfs_25_june"
os.makedirs(main_download_dir, exist_ok=True)

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        return document.querySelector('downloads-manager')
        .shadowRoot.querySelector('#downloadsList')
        .items.filter(e => e.state === 'COMPLETE')
        .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
    """)

# Function to wait for downloads to complete
def download_wait(download_dir):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 600:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(download_dir):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds

# Set up Selenium WebDriver options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
prefs = {
    "download.default_directory": os.path.join(os.getcwd(), main_download_dir),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# Read URLs from CSV file
urls = "./pdf_links_processing - failed_10_june.csv"
data = pd.read_csv(urls, encoding='latin1')  # Read CSV into a DataFrame named 'data'

# Function to download PDF by direct link
def pdf_extension(link, file_number, sub_dir):
    driver.get(link)
    print(f"Processing PDF extension link: {link}")
    driver.maximize_window()
    time.sleep(2)

    file_downloaded = download_wait(main_download_dir)
    if file_downloaded:
        for filename in os.listdir(main_download_dir):
            if filename.endswith('.pdf'):
                old_file_path = os.path.join(main_download_dir, filename)
                new_file_name = f"{file_number}.pdf"
                new_file_path = os.path.join(sub_dir, new_file_name)
                shutil.move(old_file_path, new_file_path)
                file_number += 1
                print("File downloaded and renamed")
    else:
        print(f"File download timed out for: {link}")
    return file_number

def non_pdf_extension(link, file_number, sub_dir):
    driver.get(link)
    print(f"Processing non-PDF extension link: {link}")

    driver.maximize_window()
    time.sleep(3)
    try:
        file_downloaded = download_wait(main_download_dir)
        if file_downloaded:
            for filename in os.listdir(main_download_dir):
                if filename.endswith('.pdf'):
                    old_file_path = os.path.join(main_download_dir, filename)
                    new_file_name = f"{file_number}.pdf"
                    new_file_path = os.path.join(sub_dir, new_file_name)
                    shutil.move(old_file_path, new_file_path)
                    file_number += 1
                    print("File downloaded and renamed")
        else:
            print(f"File download timed out for: {link}")
    except Exception as e:
        print(f"Error during file download: {e}")
    return file_number

def handle_iframe(file_number, sub_dir):
    iframe_links = []
    iframes = driver.find_elements(By.XPATH, '//iframe')
    for iframe in iframes:
        iframe_src = iframe.get_attribute("src")
        if iframe_src:
            iframe_links.append(iframe_src)
    driver.switch_to.default_content()
    print(f"PDF links found in iframes: {len(iframe_links)}")
    print(iframe_links)

    for pdf_link in iframe_links:
        if pdf_link.endswith(".pdf"):
            driver.get(pdf_link)
            time.sleep(15)
            file_number = pdf_extension(pdf_link, file_number, sub_dir)
    return file_number

def handle_municode(start_url, sub_dir, file_number):
    if "municode.com" not in start_url:
        print(f"URL does not contain municode.com: {start_url}")
        return file_number
    
    parsed_url = urlparse(start_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    print(base_url)

    driver.get(start_url)
    time.sleep(5)

    # Close the hopscotch bubble if present
    try:
        hopscotch_bubble_close_button = driver.find_element(By.XPATH, "//div[@class='hopscotch-bubble-container']/button[@class='hopscotch-bubble-close hopscotch-close']")
        hopscotch_bubble_close_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print("No hopscotch bubble found to close.")

    # Find main_headings and sub_headings
    main_headings = driver.find_elements(By.XPATH, '//li[@ng-repeat="node in toc.topLevelNodes track by node.Id"]/a[@class="toc-item-heading"]')
    sub_headings = driver.find_elements(By.XPATH, "//ul[starts-with(@data-ng-if, 'node.isExpanded && node.Children.length')]/li[starts-with(@id,'genToc_')]/a[starts-with(@href,'https')]")
    print(f"Main headings found: {len(main_headings)}")
    print(f"Sub headings found: {len(sub_headings)}")

    def find_iframes_and_download(links):
        iframe_links = []
        for link in links:
            try:
                link.click()
                time.sleep(2)
                iframes = driver.find_elements(By.XPATH, '//iframe')
                for iframe in iframes:
                    iframe_src = iframe.get_attribute("src")
                    if iframe_src and iframe_src.endswith(".pdf") and iframe_src not in iframe_links:
                        iframe_links.append(iframe_src)
                driver.switch_to.default_content()
            except (NoSuchElementException, WebDriverException) as e:
                print(f"Error processing link: {e}")
                continue
        return iframe_links

    # Check main heading links for iframes
    iframe_links = find_iframes_and_download(main_headings)

    # If no iframes found in main heading links, check in sub heading
    if not iframe_links:
        iframe_links = find_iframes_and_download(sub_headings)

    print(f"PDF links found in iframes: {len(iframe_links)}")
    print(iframe_links)

    for pdf_link in iframe_links:
        driver.get(pdf_link)
        time.sleep(15)
        file_number = pdf_extension(pdf_link, file_number, sub_dir)

    return file_number

def process_urls(data):
    for index, row in data.iterrows():
        try:
            start_url = row['link']
            region_slug = row['region_slug']
            state_code = row['state_code']
            # Skip URLs containing "ecode", "codepublishing", or "municipal.codes etc.."
            if any(substring in start_url for substring in ["ecode", "codepublishing", "municipal.codes", "codelibrary.amlegal", "encodeplus"," municipalcodeonline", "qcode","town.codes","drive.google"]):
                print(f"Skipping URL: {start_url}")
                continue

            if start_url and region_slug and state_code:
                sub_dir_name = f"{region_slug}-{state_code}"
                sub_dir = os.path.join(main_download_dir, sub_dir_name)
                os.makedirs(sub_dir, exist_ok=True)

                file_number = 1

                if "municode.com" in start_url:
                    file_number = handle_municode(start_url, sub_dir, file_number)
                else:
                    driver.get(start_url)
                    driver.maximize_window()
                    
                    parsed_url = urlparse(start_url)
                    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    print(base_url)

                    pdf_links = []
                    non_pdf_links = []

                    time.sleep(10)
                    all_links = driver.find_elements(By.TAG_NAME, "a")
                    for link in all_links:
                        href = link.get_attribute("href")
                        #if href:
                        if href (link.startswith("http://") or link.startswith("https://")):
                            if base_url in href:
                                if href.endswith(".pdf"):
                                    if href not in pdf_links:
                                        pdf_links.append(href)
                                elif href not in non_pdf_links:
                                    non_pdf_links.append(href)

                    for link in pdf_links:
                        try:
                            file_number = pdf_extension(link, file_number, sub_dir)
                        except Exception as e:
                            print(f"Error processing PDF extension link {link}: {e}")

                    for link in non_pdf_links:
                        try:
                            file_number = non_pdf_extension(link, file_number, sub_dir)
                        except Exception as e:
                            print(f"Error processing non-PDF extension link {link}: {e}")

                    # Handle iframes if no PDFs were downloaded
                    if file_number == 1:
                        file_number = handle_iframe(file_number, sub_dir)

        except WebDriverException as e:
            print(f"Error processing row {index} with URL {row['link']}: {e}")
        except Exception as e:
            print(f"Unexpected error processing row {index} with URL {row['link']}: {e}")

process_urls(data)
driver.quit()