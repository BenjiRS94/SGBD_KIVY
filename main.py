# -*- encoding: utf-8 -*-

import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from kivy.uix.accordion import Accordion, AccordionItem

from kivy.network.urlrequest import UrlRequest

from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class Login(BoxLayout):
    pass

    def randomFunction(self, t1, t2):
        print 'transition! GO'
        

class NewObject(BoxLayout):
    pass

    def randomFunction(self, t1, t2, t3):
        print 'NewObject : randomFunction'
        print t1
        print t2
        print t3
        # print lt0.theTxt.text


class AtumObject(BoxLayout):
    pass


class FindObjectsForm(BoxLayout):
    pass


class FindObjectsResult(BoxLayout):
    pass

    def __init__(self, **kwargs):
        super(FindObjectsResult, self).__init__(**kwargs)

        self.l = Label(text = "Prova")


class FindObjects(BoxLayout):
    pass

    def __init__(self, **kwargs):
        super(FindObjects, self).__init__(**kwargs)

        self.first = FindObjectsForm()

        self.second = FindObjectsResult()

        self.add_widget(self.first)


    def executeRequest(self, t1, t2, t3):
        self.clear_widgets()
        print 'FindObjects : executeRequest'
        print t1
        print t2
        print t3
        self.add_widget(self.second)
#         self.got_json(req)


#     def got_json(req, result):
#         for key, value in result['headers'].items():
#             print('{}: {}'.format(key, value))
# 
# req = UrlRequest('https://httpbin.org/headers', got_json)

# Aquesta classe està de prova per quan una llista té només un element ja que 
# sinó ocuparia tota la pantalla i és lleig
class Row(BoxLayout):
    pass




class InterfaceManager(BoxLayout):

    def __init__(self, **kwargs):
        super(InterfaceManager, self).__init__(**kwargs)

        self.first = Login()

        self.second = Accordion()
        self.second = Accordion(orientation='vertical')
        options = ['My profile', 'New Object', 'Find Objects']

        for key in options:
            item = AccordionItem(title='%s' % key)
            if key == 'New Object': 
                    item.add_widget(NewObject())
            if key == 'Find Objects':
                    item.add_widget(FindObjects())

            self.second.add_widget(item)


        self.final = Label(text="Hello World")
        self.add_widget(self.first)

    def show_second(self, usr, pss):
        self.clear_widgets()
        print 'show_second!!!'
        print usr
        print pss
        self.add_widget(self.second)

    def show_final(self, button):
        self.clear_widgets()
        self.add_widget(self.final)


class sgbdApp(App):
    def build(self):
        return InterfaceManager(orientation='vertical')

if __name__ == '__main__':
    sgbdApp().run()
