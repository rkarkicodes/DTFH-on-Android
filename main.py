from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition,TransitionBase
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty
# from jnius import autoclass
from kivy.clock import Clock
import json

def epis():
    with open("episodes.json") as json_file:
        json_data = json.load(json_file)
    return json_data


class Podcastback(GridLayout):
    pass


class NowPlaying(Screen):
    pass
class ScreenManagement(ScreenManager):



    player=ObjectProperty()
    state=StringProperty()




    def play(self):
        if self.state=='play':
            #pause
            self.player.pause()
            self.state='pause'

            Clock.unschedule(self.seek)
        else:
            #play
            self.player.start()
            self.state='play'

            Clock.schedule_interval(self.seek,1.0)





    def now_playing(self,scr,aud):

        if self.screen_names[1]=="NowPlaying":
            ##load new episode first play
            self.screens[1]=self.screens[-1]
            MediaPlayer = autoclass('android.media.MediaPlayer')
            self.player=MediaPlayer()
            self.player.setDataSource(aud)
            self.player.prepare()
            self.screens[1].ids.slider.max=(self.player.getDuration()/1000.0)


            self.play()
            print self.screen_names

        elif self.screen_names[1]!=scr:
            ##load new episode
            self.screens[1]=self.screens[-1]
            self.player.stop()
            self.player.reset()
            self.player.setDataSource(aud)
            self.player.prepare()
            self.screens[1].ids.slider.max=(self.player.getDuration()/1000.0)
            self.screens[1].ids.slider.value=0
            self.state='pause'
            self.play()

            print "exchange"


        elif self.screen_names[1]==scr and self.state=='play':
            #pause current episode
            self.play()

        elif self.state=='pause':
            #play paused episode
            self.play()




    def forward(self):
        self.player.seekTo(self.player.getCurrentPosition()+15000)

    def rewind(self):
        self.player.seekTo(self.player.getCurrentPosition()-15000)



    def unschedule(self):
        pass

    def seek(self,dt):
        # self.seek_pos+=self.seek_unit
        self.screens[1].ids.slider.value=(self.player.getCurrentPosition()/1000.0)
        self.screens[1].ids.forward.text=str(self.player.getCurrentPosition()/1000.0)
        self.screens[1].ids.rewind.text=str(self.screens[1].ids.slider.value)





    def episode_page(self,snumber,sinfo,spicture,slink):
        name= str(snumber)

        scr=EpisodePage(name=name,info=sinfo,picture=spicture,audio=slink)
        self.add_widget(scr)
        self.current=name
        print self.screen_names


    def rem(self,scr):

        if len(self.screen_names)!=2:
            self.remove_widget(self.screens[-1])
            print self.screen_names
        elif scr.name==self.screen_names[1]:

            print self.screen_names

    def play_button(self):
        if self.screen_names[1]!="NowPlaying":
            self.current=self.screen_names[1]

        elif len(self.screens)==3:
            print "last"
            self.current=self.screen_names[-1]
        else:
            print "first"
            self.current=self.screen_names[0]


class MainScreen(Screen):

    pass


class EpisodePage(Screen):
    name=StringProperty()
    info=StringProperty()
    picture=StringProperty()
    audio=StringProperty()


    def stop(self):
        self.sound.player.stop()
        self.sound.player.unload()
    def button_change(self):

        if self.ids.play.img=="player/play.png":
            self.ids.play.img="player/pause.png"
        else:
            self.ids.play.img="player/play.png"


class EpisodeList(ScrollView):
    def __init__(self,*args,**kwargs):
        super(EpisodeList, self).__init__(*args, **kwargs)

    def load_epis(self):
        for epi in epis():

            self.children[0].add_widget(Episode(epi[0],epi[1],epi[2],epi[3],epi[4]))

    def sub(self,l):
        if l==0.0:

            self.load_epis()



class Episode(GridLayout,object):

    screen=ObjectProperty()

    def __init__(self,number,title,picture,info,audiolink,*args,**kwargs):
        self.number=number
        self.title=title
        self.picture=picture
        self.info=self.check(info)
        self.audioLink=audiolink
        super(Episode, self).__init__(*args, **kwargs)


    def check(self,info):
        if info==None:
            return ''
        else:
            return info


class EpisodeAudio(BoxLayout):
    pass



class PodcastApp(App):
    def on_pause(self):
        return True


if __name__=='__main__':
	PodcastApp().run()