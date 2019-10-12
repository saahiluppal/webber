import requests
from bs4 import BeautifulSoup

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
print(spell_title)

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
print(spell_description)

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
print(entity_titles)

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
print(entity_types)

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
print(entity_description)

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
print(entity_url)

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
print(entity_wikipedia)

## Third Part Loading webpages
