from entity import Entity
from web_results import Web_results
import webbrowser
import os
import time
from color import Color

color = Color()

def entity_function(query):
    os.system('clear')
    entity_res = Entity(query)
    if not entity_res.get_title():
        return False
    title = entity_res.get_title()[0] 
    typee = entity_res.get_type()[0] if entity_res.get_type() else 'Unknown'
    url = entity_res.get_url()[0] if entity_res.get_url() else 'Unknown'
    description = entity_res.get_description()[0] if entity_res.get_description() else 'Unknown'
    wikipedialink = entity_res.get_wikipedia_link()[0] if entity_res.get_wikipedia_link() else 'Unknown'
    textunder = entity_res.get_wikipedia_link()[1] if entity_res.get_wikipedia_link() else 'Unknown'
    if entity_res.get_spell_title():
        return [color.RED+entity_res.get_spell_title()+color.END,color.RED+entity_res.get_spell_description()+color.END,'\n',
            "Title :: "+title,"Type :: "+typee,url,color.YELLOW+description+color.END,
        color.BLUE+"Wikipedia :: "+wikipedialink+color.END,color.BLUE+"Text Under :: "+textunder+color.END]
    else:
        return ["Title :: "+title,"Type :: "+typee,url,color.YELLOW+description+color.END,
        color.BLUE+"Wikipedia :: "+wikipedialink+color.END,color.BLUE+"Text Under :: "+textunder+color.END]

def web_function(query):
    web_res = Web_results(query)
    if not web_res.get_site_title():
        webbrowser.open('https://www.entireweb.com/web?q='+query)
        return False
    print_web(web_res)

def print_web(web_res):
    title = web_res.get_site_title()
    url = web_res.get_site_url()
    description = web_res.get_site_description()

    for i,j,k in zip(title,url,description):
        print(color.BOLD+i+color.END)
        print(j)
        print(k)
        print()



while True:
    query = input('Query :: ')
    if query=='exit' or query=='break' or query=='quit':
        break
    entity_results = entity_function(query)
    print()
    if entity_results:
        for i in entity_results:
            if i:
                print(i)
        print()
        time.sleep(3)
        web_function(query)
    elif entity_results==False:
        time.sleep(3)
        web_function(query)