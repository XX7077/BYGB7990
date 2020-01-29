#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple script that shows how beautiful soup is used
"""

# 1. Import some useful libraries
import requests
import re
from bs4 import BeautifulSoup

# 2. Get the website data

# use requests to get the website
result = requests.get("http://www.apostolos-filippas.com/")

# store the webpage content to a variable
src = result.content

# create a BS object
soup = BeautifulSoup(src)

# 3. Use BS to parse and process

# 3.1 Get a list of all sections

# get sections
sections = soup.find_all('section')

# see the attributes of each section
for section in sections:
    print(section.attrs)
    
# get all links (href) and link text in the "home" section
for section in sections:
    if section.attrs['id']=='home':
        # we can use the find_all for every BS item!!!
        for link in section.find_all('a'):
            print("Link: "+link.attrs['href'] + ' text: ' + link.text)
        break

# 3.2 Find all of AF's papers

#   find all links contained in the page
links = soup.find_all("a")
    
#   find all of the paper titles is now easy!
for link in links:
    if "papers" in link.attrs['href']:
        # of course, you have to find the correct BS method
        print(link.string)


# 3.3 Alternative way to do this

# you can use findAll to search for  elements with specific attributes
sections = soup.findAll('section', {'id':re.compile('home')})

# find all of my papers!
papers = soup.findAll('a', {'href':re.compile('papers/.+')})
for paper in papers:
    print(paper.text)

             
''' 
Notes

(1) To print a prettier soup, use print(soup.prettify())
    The outcome may be easier for you to parse!
    
(2) BS has a lot of other useful features. In the optional readings, 
    I link to a tutorial that will allow you to learn more

'''