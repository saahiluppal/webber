from load_page import Load_page
from entity import Entity

class Web_results:
    def __init__(self,query):
        entity = Entity(query)
        self.soup = entity.return_soup()

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


if __name__ == '__main__':
    webresults = Web_results(input('query'))
    print(webresults.get_site_title())
    print(webresults.get_site_url())
    print(webresults.get_site_description())
    print(len(webresults.get_site_description()))
    print(len(webresults.get_site_title()))
    print(len(webresults.get_site_url()))