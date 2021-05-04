#Import Dependencies
from splinter import Browser
from pandas as pd
from bs4 import BeautifulSoup as bs
import os
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
import warnings
warnings.filterwarnings('ignore')

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

#Create Mission to Mars Dictionary
mars_information = {}

def scrape_mars_news():
    #Initialize Browser
    browser = init_browser()

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    soup = bs(html, 'html parser')
    news_title = soup.find('div', class_='content_title').find('a').text
    news_para = soup.find('div', class_='article_teaser_body').text

    mars_information['news_title'] = news_title
    mars_information['news_paragraph'] = news_para

    return mars_information

    browser.quit()
     
     #Image
def scrape_mars_image():

    #Initialize Browser
    browser = init_browser()

    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(featured_image_url)

    html_image = browser.html

    soup = bs(html_image, 'html.parser')

    # image_url = soup.find('article')['style'].replace('background-image: url(','').replace('')[1:-1]

    web_url = 'https://www.jpl.nasa.gov'
    
    #Concatenate website and scraped url
     image_url = web_url +  image_url

     image_url

     #Dictionary entry
     mars_information['image_url'] = image_url

     browser.quit()

     return mars_information

 
 ### Mars Fact

    # Scrape Mars facts 
    url='https://space-facts.com/mars/'
    tables=pd.read_html(url)
    
    mars_fact=tables[0]
    mars_fact=mars_fact.rename(columns={0:"Profile",1:"Value"},errors="raise")
    mars_fact.set_index("Profile",inplace=True)
    mars_fact
    
    fact_table=mars_fact.to_html()
    fact_table.replace('\n','')
    
    ### Mars Hemispheres

    # Scrape Mars hemisphere title and image
    other_url='https://astrogeology.usgs.gov'
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    # Extract hemispheres item elements
    mars_hems=soup.find('div',class_='collapsible results')
    mars_item=mars_hems.find_all('div',class_='item')
    hemisphere_image_urls=[]

    # Loop through each hemisphere item
    for item in mars_item:
        # Error handling
        try:
            # Extract title
            hem=item.find('div',class_='description')
            title=hem.h3.text
            # Extract image url
            hem_url=hem.a['href']
            browser.visit(other_url+hem_url)
            html=browser.html
            soup=bs(html,'html.parser')
            image_src=soup.find('li').a['href']
            if (title and image_src):
                # Print results
                print('-'*50)
                print(title)
                print(image_src)
            # Create dictionary for title and url
            hem_dict={
                'title':title,
                'image_url':image_src
            }
            hemisphere_image_urls.append(hem_dict)
        except Exception as e:
            print(e)

    # Create dictionary for all info scraped from sources above
    mars_dict={
        "news_title":news_title,
        "news_para":news_para,
        "featured_image_url":featured_image_url,
        "fact_table":fact_table,
        "hemisphere_images":hemisphere_image_urls
    }
    # Close the browser after scraping
    browser.quit()
    return mars_dict