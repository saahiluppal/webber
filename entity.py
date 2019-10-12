from load_page import Load_page
from bs4 import BeautifulSoup
from color import Color
import os

class Entity:
    def __init__(self,query):
        self.parsed_page = Load_page(query)
        self.soup = self.parsed_page.get_soup()
        
    def get_title(self):
        total_entities = self.soup.find('div',{'class':'entity-results'})
        if total_entities==None:return False
        self.entity_results = []
        for i in total_entities:
            if self.soup.find('div',{'class':'entity-results','class':'entity-title'})==None:return False
            result = self.soup.find('div',{'class':'entity-results','class':'entity-title'}).text
            if result not in self.entity_results:
                self.entity_results.append(result)
        return self.entity_results

    def get_type(self):
        total_entities = self.soup.find('div',{'class':'entity-results'})
        if self.soup.find('div',{'class':'entity-results'})==None:return False
        self.entity_results = []
        for i in total_entities:
            if self.soup.find('div',{'class':'entity-results','class':'entity-type'})==None:return False
            result = self.soup.find('div',{'class':'entity-results','class':'entity-type'}).text
            if result not in self.entity_results:
                self.entity_results.append(result)
        return self.entity_results

    def get_description(self):
        total_entities = self.soup.find('div',{'class':'entity-results'})
        if total_entities==None:return False
        self.entity_results = []
        for i in total_entities:
            if self.soup.find('div',{'class':'entity-results','class':'entity-description'})==None:return False
            result = self.soup.find('div',{'class':'entity-results','class':'entity-description'}).text
            try:    result = result.replace('\n','')
            except: pass
            try:    result = result.replace('Read more','')
            except: pass
            result = result.strip()
            if result not in self.entity_results:
                self.entity_results.append(result)
        return self.entity_results

    def get_url(self):
        if self.soup.find('div',{'class':'entity-section','class':'entity-url'})==None:return False
        total_entities = self.soup.find('div',{'class':'entity-section','class':'entity-url'}).find_all('a')
        self.entity_results = []
        for i in total_entities:
            result = i.get('href')
            if result not in self.entity_results:
                self.entity_results.append(result)
        return self.entity_results

    def get_wikipedia_link(self):
        if self.soup.find('div',{'class':'entity-content','class':'entity-contract'})==None:return False
        total_entities = self.soup.find('div',{'class':'entity-content','class':'entity-contract'}).find_all('a')
        self.entity_results = []
        for i in total_entities:
            result = i.get('href')
            if result not in self.entity_results:
                self.entity_results.append(result)
        return self.entity_results

    def return_soup(self):
        return self.soup
        
    def get_spell_title(self):
        return self.parsed_page.get_spell_title()
        
    def get_spell_description(self):
        return self.parsed_page.get_spell_description()

# for testing purpose
if __name__ == "__main__":

    entity = Entity(input('Query:: '))
    if not entity.get_title():
        print('Results Not Found!..')
        exit()
    
    color = Color()
    os.system('clear')
    if entity.get_spell_title():
        print()
        print(color.GREEN+entity.get_spell_title()+color.END)
    if entity.get_spell_description():
        print(color.RED+entity.get_spell_description()+color.END)
    print()
    print(f'Title     ::  {entity.get_title()[0]}')
    type_ = entity.get_type()[0] if entity.get_type() else "Unknown"
    print(f'Type      ::  {type_}')
    description = entity.get_description()[0] if entity.get_description() else "Unknown"
    print('\nDescription :: '+color.YELLOW+f'{description}'+color.END)
    print()
    url = entity.get_url()[0] if entity.get_url() else "Unknown"
    print(f'URL        ::  {url}')
    wikipedia = entity.get_wikipedia_link()[0] if entity.get_wikipedia_link() else "Unknown"
    print(f'Wikipedia  ::  {wikipedia}\n')

    