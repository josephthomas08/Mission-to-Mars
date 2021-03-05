#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup 
import pandas as pd


# In[26]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[27]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[28]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[29]:


# 2A Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[30]:


# 2B
html = browser.html
image_soup = soup(html, 'html.parser')
links = browser.find_by_css("a.product-item h3")


# In[31]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(len(links)):

    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[32]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[33]:


# 5. Quit the browser
browser.quit()


# In[ ]:




