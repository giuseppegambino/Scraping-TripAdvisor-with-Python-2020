# Scraping TripAdvisor with Python 2020 *

Python implementation of web scraping of TripAdvisor with Selenium in a new 2020 website.

There are two scripts:
  - "restaurants_scraper.py" to scrape restaurant
  - "things_to_do_scraper.py" to scrape attraction and monuments
  
The python function is commented, write me if you have doubts.

Features implemented: 
  - The click function to open the "more" button of the reviews 
  - The click function to change the page
  - Csv file with the date, the score, the title and the full review!
  
What I used:
  - Python 3.8.2
  - Selenium 3.141.0
  - Safari 14.0.1
  - Visual Studio Code 1.51.1
  - Macbook Pro 13" M1 2020 with macOS Big Sur 11.0.1
  
How to use: 
  First approach: download the python file, open it with a text editor and edit the default field (csv file path, number of pages, tripadvisor url)
  
  Second approach: download the file and launch it directly from the terminal, passing:
      - the path of your csv file where the reviews will be stored
      - the number of pages of the desired website that you want to scrape
      - the url of tripadvisor website that you want to scrape

Example: python3 /Users/gius/Desktop/Script/tripadvisor/things_to_do_scraper.py desktop/reviews.csv 50 https://www.tripadvisor.com/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html

*This activity has been supported by a grant from the Project IDEHA - PON "Ricerca e Innovazione" 2014-2020 - Innovation for Data Elaboration in Heritage Areas, Azione II
