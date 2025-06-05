from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the driver
driver = webdriver.Chrome()

# Load the starting page
driver.get("https://ecode360.com/9403853")

# Extract the span elements with class "titleNumber"
headings_elements = driver.find_elements(By.XPATH, '//span[@class="titleNumber" and contains(normalize-space(.), "Article")]')

# print(span_elements)


# Extract hrefs from their ancestor <a> tags
links = []
for heading_element in headings_elements:
    try:
        parent_a = heading_element.find_element(By.XPATH, './ancestor::a[1]')
        href = parent_a.get_attribute('href')
        if href:
            links.append(href)
    except:
        pass

# Dictionary to store content against each link
content_dict = {}
sub_links = []
# Loop through each link
for link in links:
    print("link",link)
    try:
        driver.get(link)
        time.sleep(2)  # Wait for page to load. Consider WebDriverWait for dynamic content
        # //div[@id="childContent"]/div[@class="section_content content"]/div
        sub_headings_elements = driver.find_elements(By.XPATH, "//*[@href[contains(., '#940385')]]")
        print(len(sub_headings_elements))
        for sub_heading_element in sub_headings_elements:
            try:
                # parent_b = sub_heading_element.find_element(By.XPATH, './ancestor::a')
                href_2 = sub_heading_element.get_attribute('href')
                # print("Type of href2",type(href_2))
                sub_links.append(href_2)
                # href_2 = parent_b.get_attribute('href')
                driver.get(href_2)
                content = driver.find_element(By.XPATH, '//div[@id="childContent"]/div[@class="section_content content"]/div').text
                print("content",content)

                    
            except:
                pass
    except Exception as e:
        content_dict[link] = f"Error: {str(e)}"