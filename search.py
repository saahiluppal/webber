import requests
from bs4 import BeautifulSoup
from color import Color
import os

query = input("Query:: ")
parser = 'lxml'

## First part Loading the page
response = requests.get('https://www.entireweb.com/web?q='+query)

# Finding Soup and decomposing advertisements
content = response.content
soup = BeautifulSoup(content,parser)
advertisements = soup.find_all('div',{'class':'web-results lastad'})
for i in advertisements:
    i.decompose()

# Getting Spell title
if soup.find('div',{'class':'web-results','class':'query-spell'}) == None:
    spell_title = False
else:
    spell_title = soup.find('div',{'class':'web-results','class':'query-spell','class':'spell-title'}).text
    try: 
        spell_title = spell_title.replace('\n','')
    except:
        pass
    spell_title = spell_title.strip()

# Getting spell description
if soup.find('div',{'class':'web-results','class':'query-spell'}) == None:
    spell_description = False
else:
    spell_description = soup.find('div',{'class':'web-results','class':'query-spell','class':'spell-description'}).text
    try:  
        spell_description = spell_description.replace('\n','')
    except:
        pass
    spell_description = spell_description.strip()

## Second part loading the entity
# Getting entity title else empty list
total_entities = soup.find('div',{'class':'entity-results'})

if total_entities==None:
    entity_titles = []
else:
    entity_titles = []
    for i in total_entities:
        if soup.find('div',{'class':'entity-results','class':'entity-title'})==None:
            entity_titles = []
        else:
            result = soup.find('div',{'class':'entity-results','class':'entity-title'}).text
            if result not in entity_titles:
                entity_titles.append(result)

# Getting entity type else empty list
if total_entities==None:
    entity_types = []
else:
    entity_types = []
    for i in total_entities:
        if soup.find('div',{'class':'entity-results','class':'entity-type'})==None:
            entity_types = []
        else:
            result = soup.find('div',{'class':'entity-results','class':'entity-type'}).text
            if result not in entity_types:
                entity_types.append(result)

# Getting entity description else empty list
if total_entities==None:
    entity_description = []
else:
    entity_description = []
    for i in total_entities:
        if soup.find('div',{'class':'entity-results','class':'entity-description'})==None:
            entity_description = [] 
        else:
            result = soup.find('div',{'class':'entity-results','class':'entity-description'}).text
            try:    result = result.replace('\n','')
            except: pass
            try:    result = result.replace('Read more','')
            except: pass
            result = result.strip()
            if result not in entity_description:
                entity_description.append(result)

# Getting url else emtpy list
if soup.find('div',{'class':'entity-section','class':'entity-url'})==None:
    entity_url = []
else:
    total_entities = soup.find('div',{'class':'entity-section','class':'entity-url'}).find_all('a')
    entity_url = []
    for i in total_entities:
        result = i.get('href')
        if result not in entity_url:
            entity_url.append(result)

# Getting wikipedia link
if soup.find('div',{'class':'entity-content','class':'entity-contract'})==None:
    entity_wikipedia = []
else:
    total_entities = soup.find('div',{'class':'entity-content','class':'entity-contract'}).find_all('a')
    entity_wikipedia = []
    for i in total_entities:
        result = i.get('href')
        if result not in entity_wikipedia:
            entity_wikipedia.append(result)

## Third Part Loading webpages
# Getting site titles else emtpy list
total_results = soup.find('div',{'class':'web-results'})
if total_results==None:
    site_titles = []
else:
    total_results = soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
    site_titles = []
    for i in total_results:
        result = i.find('div',{'class':'site-title'}).text
        site_titles.append(result)

# Getting site urls else empty list
if total_results == None:
    site_urls = []
else:
    total_results = soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
    site_urls = []
    for i in total_results:
        result = i.find('div',{'class':'site-url'}).find('a')
        site_urls.append(result.get('href'))

# Getting site descriptions else empty list
if total_results == None:
    site_descriptions = []
else:
    total_results = soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
    site_descriptions = []
    for i in total_results:
        result = i.find('div',{'class':'site-description'}).text
        site_descriptions.append(result)


# Third Part Stacking all of these results in a beautiful way
# site title
# site url
# site description

color = Color()
os.system('clear')

if spell_title:
    print()
    print(color.GREEN + spell_title + color.DEFAULT)
    print(color.RED + spell_description + color.DEFAULT)

if entity_titles:
    print()
    print("Title  ::   ",entity_titles[0])
    print("Type   ::   ",entity_types[0] if entity_types else "Unknown")
    print('\nDescription :: '+color.YELLOW +entity_description[0] + color.DEFAULT+'\n' if entity_description else "Unknown")
    print("URL       :: ",entity_url[0] if entity_url else "Unknown")
    print("Wikipedia :: ",entity_wikipedia[0]+'\n' if entity_wikipedia else "Unknown\n")

if site_titles:
    print()
    for title,url,description in zip(site_titles,site_urls,site_descriptions):
        print(color.BOLD + title + color.DEFAULT)
        print(color.CYAN + url + color.DEFAULT)
        print(description) 
        print()