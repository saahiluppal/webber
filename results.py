from load_page import Load_page
from color import Color
import os

class Web_results:
    def __init__(self,query):
        self.parsed_page = Load_page(query)
        self.soup = self.parsed_page.get_soup()

    def get_site_title(self):
        total_results = self.soup.find('div',{'class':'web-results'})
        if total_results==None:return False
        total_results = self.soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
        self.site_results = []
        for i in total_results:
            result = i.find('div',{'class':'site-title'}).text
            self.site_results.append(result)
        return self.site_results

    def get_site_url(self):
        total_results = self.soup.find('div',{'class':'web-results'})
        if total_results == None:return False
        total_results = self.soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
        self.site_results = []
        for i in total_results:
            result = i.find('div',{'class':'site-url'}).find('a')
            self.site_results.append(result.get('href'))
        return self.site_results

    def get_site_description(self):
        total_results = self.soup.find('div',{'class':'web-results'})
        if total_results == None: return False
        total_results = self.soup.find('div',{'class':'web-results'}).find_all('div',{'class':'site-result'})
        self.site_results = []
        for i in total_results:
            result = i.find('div',{'class':'site-description'}).text
            self.site_results.append(result)
        return self.site_results
    
    def get_spell_title(self):
        return self.parsed_page.get_spell_title()
        
    def get_spell_description(self):
        return self.parsed_page.get_spell_description()


if __name__ == '__main__':
    
    webresults = Web_results(input('Query:: '))
    color = Color()
    os.system('clear')

    if webresults.get_spell_title():
        print()
        print(color.GREEN + webresults.get_spell_title() + color.END)
    if webresults.get_spell_description():
        print(color.RED + webresults.get_spell_description() + color.END)

    try: epochs = len(webresults.get_site_title())
    except: print("Results Not Found!...");exit()
    print()
    for epoch in range(epochs):
        print(color.BOLD + webresults.get_site_title()[epoch] + color.END)
        print(color.CYAN + webresults.get_site_url()[epoch] + color.END)
        print(webresults.get_site_description()[epoch])
        print()