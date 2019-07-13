import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.entireweb.com/web?q=hide')

soup = BeautifulSoup(response.content,'lxml')

title = soup.find('div',{'class':'rc-anchor-center-container'}).find('label',{'id':'recaptcha-anchor-label'}).find('span',{'arina-live':'polite'}).text

print(title)