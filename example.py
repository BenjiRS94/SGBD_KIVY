from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App

import requests

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window


from kivy.uix.textinput import TextInput


def randomRequest(item):
	r = requests.get('https://opendata.somenergia.coop/v0.2/members/by/country/on/2018-10-01')
	item.add_widget(Label(text=r.text))


def randomFunction(item):
	item.add_widget(Label(text=u'Specific Option Screen'))


from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        Clock.schedule_interval(self.my_callback, 0.5)

        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False, text='caca')
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        #self.button = DemoBox(usr=self.username.text, psw=self.password)
        self.button = DemoBox()
        #self.button.myFunc(usr=self.username.text, psw=self.password)
        self.add_widget(self.button)


    def my_callback(self, a):
    	self.remove_widget(self.button)
    	self.button = DemoBox()
    	self.button.myFunc(usr=self.username.text, psw=self.password)
    	self.add_widget(self.button)
    	



from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from functools import partial


class DemoBox(BoxLayout):

    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        #self.myFunc(**kwargs)

    def myFunc(self, usr, psw):
        btn1 = Button(id="Sender", text="Send",
        	font_size=30,
        	pos_hint={'x': .75, 'center_y': .5},
        	size_hint=(.5, .5),
        	on_release = partial(self.callback, x=usr, y=psw)
        )
        #btn1.bind(on_press=partial(self.callback, x=usr, y=psw))
        self.add_widget(btn1)

    def callback(self, obj, x, y):
        print("callback: x=", x)
        print("callbock: y=", y)



class AccordionApp(App):
    def build(self):
        root = Accordion()
        root = Accordion(orientation='vertical')
        options = ['My profile', 'Sell Object', 'Find Objects']
        for option in options:
            item = AccordionItem(title='%s' % option)

            item.add_widget(LoginScreen())

            root.add_widget(item)

        return root


if __name__ == '__main__':
    AccordionApp().run()
