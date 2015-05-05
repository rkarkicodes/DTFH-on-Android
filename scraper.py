import requests
from BeautifulSoup import BeautifulSoup
import HTMLParser
from kivy.uix.button import Button

import json

dic=[]

class episodeObject(object):

    def __init__(self,link):
        self.title=""
        self.picture=""
        self.info=""
        self.audioLink=""
        self.createEpisode(link)

    def createEpisode(self,link):

        response=BeautifulSoup((requests.get(link)).content)


        self.title=HTMLParser.HTMLParser().unescape((response.findAll("title")[0].string).split("|")[1]).encode('utf-8')

        self.ep=(response.find("div", id="content").h1.text).split(":")[0]

        self.picture=response.find("div", id="content").img['src']
        self.info=response.find("div", id="content").h4.findNextSibling().string
        self.audioLink=response.find("a", title="Play").get('href')
        dic.append([self.ep,self.title,self.picture,self.info,self.audioLink])


def createEpisodes():
    i=1
    while requests.get("http://duncantrussell.com/category/podcast/page/"+str(i)+"/").status_code==200:
        ArchivePage=requests.get("http://duncantrussell.com/category/podcast/page/"+str(i)+"/")
        print i
        i+=1
        response=BeautifulSoup(ArchivePage.content)
        episodes=response.findAll("div", "eps")

        for episode in episodes:
            a=episodeObject(episode.a['href'])

    with open("episodes_new.json",mode='a') as outfile:
        json.dump(dic,outfile,sort_keys=True,indent=4,ensure_ascii=True,encoding='utf-8')

createEpisodes()


import json
import os

a=os.getcwd()+'/episodes_new.json'
print a

with open(a) as file:
    data=json.load(file)
    print sorted(data.iterkeys())
















