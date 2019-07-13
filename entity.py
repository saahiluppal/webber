from load_page import Load_page
from bs4 import BeautifulSoup

class Entity:
    def __init__(self,query):
        parsed_page = Load_page(query)
        self.soup = parsed_page.get_soup()
        
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
        
# for testing purpose
if __name__ == "__main__":
    entity = Entity(input('query'))
    print('title::',entity.get_title())
    print('type:',entity.get_type())
    print('desription:',entity.get_description())
    print('url:',entity.get_url())
    print('wikipedia link:',entity.get_wikipedia_link()[1])

    