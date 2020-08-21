from urllib.request import urlopen as req
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
url_li = []
mainurl = 'https://play.google.com/store/apps?hl=en'
loadhtml = req(mainurl)
page1 = loadhtml.read()
loadhtml.close()
bspage1 = bs(page1, "html.parser")
cat_links = bspage1.findAll("li", {"class":"KZnDLd"})
try:
    for i in range(len(cat_links)):
        url_li.append('https://play.google.com' + cat_links[i].a["href"] + '?hl=en')
    for my_url in url_li:
        load2 = req(my_url)
        page2 = load2.read()
        load2.close()
        bspage2 = bs(page2, "html.parser")
        seemores = []
        see_links = bspage2.findAll("div", {"class":"W9yFB"})
        for i in range(len(see_links)):
            seemores.append('https://play.google.com' + see_links[i].a["href"])
        
        for fiurl in seemores:
            load3 = req(fiurl)
            page3 = load3.read()
            load3.close()
            bspage3 = bs(page3, "html.parser")
            containers = bspage3.findAll("div",{"class":"ImZGtf mpg5gc"})
            container = containers[0]
            title = container.findAll("div", {"class":"WsMG1c nnK0zc"})
            owner = container.findAll("div", {"class":"KoLSrc"})
            for container in containers:
                title = container.findAll("div", {"class":"WsMG1c nnK0zc"})
                app_name = title[0].text
                owner = container.findAll("div", {"class":"KoLSrc"})
                owner_name = owner[0].text
                print("App : "+ app_name)
                print("Owner : "+ owner_name
                
                
except HTTPError as err:
    if err.code==404:
        pass
    else:
        raise
    
