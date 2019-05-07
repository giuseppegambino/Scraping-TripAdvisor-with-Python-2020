import csv
import time
from selenium import webdriver

# import the webdriver
driver = webdriver.Chrome("/Users/gius/Downloads/chromedriver74")
# inser the tripadvisor's website of one attraction 
driver.get("https://www.tripadvisor.it/Attraction_Review-g657290-d2213040-Reviews-Ex_Stabilimento_Florio_delle_Tonnare_di_Favignana_e_Formica-Isola_di_Favig.html")

# function to check if the button is on the page
from selenium.common.exceptions import NoSuchElementException        
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# open the file to save the review
csvFile = open('desktop/review.csv', 'a')
csvWriter = csv.writer(csvFile)

# not commented if you wanna select the stars (you can use more than one, dont forget the sleep function)
# time.sleep(2)
# driver.find_element_by_xpath('//label[@for="filters_detail_checkbox_trating__5"]').click()
# time.sleep(2)

for i in range(0,400):
    
    if (check_exists_by_xpath("//span[@class='taLnk ulBlueLinks']")):
        # to expand the review 
        driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()
        time.sleep(5)

    container = driver.find_elements_by_xpath("//div[@class='review-container']")

    num_page_items = len(container)
    for j in range(num_page_items):
        # to save the rating
        string = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class")
        data = string.split("_")
        # to save in a csv file readable the star and the review [Ex: 50,"I love this place"]
        csvWriter.writerow([data[3], container[j].find_element_by_xpath(".//p[@class='partial_entry']").text.replace("\n", "")])

    # to change the page
    driver.find_element_by_xpath('//a[@class="nav next taLnk ui_button primary"]').click()
    time.sleep(5)
    
driver.close()
