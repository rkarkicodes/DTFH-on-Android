# import requests
# from BeautifulSoup import BeautifulSoup
import HTMLParser
from kivy.uix.button import Button

import json
#
# dic=[]
#
# class episodeObject(object):
#
#     def __init__(self,link):
#         self.title=""
#         self.picture=""
#         self.info=""
#         self.audioLink=""
#         self.createEpisode(link)
#
#
#     def createEpisode(self,link):
#
#         response=BeautifulSoup((requests.get(link)).content)
#
#
#         self.title=HTMLParser.HTMLParser().unescape((response.findAll("title")[0].string).split("|")[1]).encode('utf-8')
#
#         self.ep=(response.find("div", id="content").h1.text).split(":")[0]
#
#         self.picture=response.find("div", id="content").img['src']
#         self.info=response.find("div", id="content").h4.findNextSibling().string
#         self.audioLink=response.find("a", title="Play").get('href')
#         dic.append([self.ep,self.title,self.picture,self.info,self.audioLink])
#
#
# def createEpisodes():
#     i=1
#     while requests.get("http://duncantrussell.com/category/podcast/page/"+str(i)+"/").status_code==200:
#         ArchivePage=requests.get("http://duncantrussell.com/category/podcast/page/"+str(i)+"/")
#         print i
#         i+=1
#         response=BeautifulSoup(ArchivePage.content)
#         episodes=response.findAll("div", "eps")
#
#         for episode in episodes:
#             a=episodeObject(episode.a['href'])
#
#     with open("episodes_new.json",mode='a') as outfile:
#         json.dump(dic,outfile,sort_keys=True,indent=4,ensure_ascii=True,encoding='utf-8')
#
# createEpisodes()
#
#
# import json
# import os
#
# a=os.getcwd()+'/episodes_new.json'
# print a
#
# with open(a) as file:
#     data=json.load(file)
#     print sorted(data.iterkeys())
#
#



# import HTMLParser
#
# a="returns to the DTFH and we talk about psychedelics and many other things&#8230;"
#
#
# l=HTMLParser.HTMLParser().unescape(a)
# print l
#
#

from mutagen.mp3 import MP3

# response=BeautifulSoup((requests.get("http://hwcdn.libsyn.com/p/3/1/b/31b0f5fcd4b5d622/dtfh_149_doblin.mp3?c_id=8693130&expiration=1428560769&hwt=ca60496fe9ee653279042a97df00ba10")).content)


import audioread
from kivy.core import audio
import json
import urllib2
import time


print dir(GstPlayer)

# GstPlayer.










# sound=SoundLoader.load("http://traffic.libsyn.com/lavenderhour/DTFH_125_rogan.mp3")
# sound=pyglet.media.StreamingSource("http://traffic.libsyn.com/lavenderhour/DTFH_125_rogan.mp3")
# print dir(sound)




# print sound


# a=sound.load("http://traffic.libsyn.com/lavenderhour/DTFH_125_rogan.mp3")
# print a


# sound.play()
#
#
# time.sleep(10)



# sound=SoundLoader.load("http://traffic.libsyn.com/lavenderhour/DTFH_148_Jack_Kornfield.mp3")
# print sound.length



# with open("episodes.json") as json_file:
#     json_data=json.load(json_file)

# sound=SoundLoader.load("http://traffic.libsyn.com/lavenderhour/DTFH_125_rogan.mp3")





# print sound.length
#
# for i in json_data:
#     try:
#         print i[-1]
#         sound=SoundLoader.load(str(i[-1]))
#         print sound.length
#         # print sound.player.get_duration()
#         sound.unload
#     except:
#         pass

# audio=audioread.audio_open("http://traffic.libsyn.com/lavenderhour/dtfh_149_doblin.mp3")
# print audio.duration