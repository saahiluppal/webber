import requests
from bs4 import BeautifulSoup

class Load_page:
    def __init__(self,query):
        self.response = requests.get('https://www.entireweb.com/web?q='+query)

    def get_soup(self,parser='lxml'):
        self.soup = BeautifulSoup(self.response.content,parser)
        advertisements = self.soup.find_all('div',{'class':'web-results lastad'})
        for i in advertisements:
            i.decompose()
        return self.soup
    
    def get_spell_title(self):
        if self.soup.find('div',{'class':'web-results','class':'query-spell'}) == None:return False
        self.spell_title = self.soup.find('div',{'class':'web-results','class':'query-spell','class':'spell-title'}).text
        try:  self.spell_title = self.spell_title.replace('\n','')
        except:pass
        return self.spell_title.strip()
        
    def get_spell_description(self):
        if self.soup.find('div',{'class':'web-results','class':'query-spell'}) == None:return False
        self.spell_description = self.soup.find('div',{'class':'web-results','class':'query-spell','class':'spell-description'}).text
        try:  self.spell_description = self.spell_description.replace('\n','')
        except: pass
        return self.spell_description.strip()


# for testing purpose
if __name__=="__main__":
    page = Load_page(input('query'))
    #print(page.get_soup().prettify())
    page.get_soup()
    print(page.get_spell_title())
    print(page.get_spell_description())

    