import time

from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import *

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivy.properties import StringProperty

mytext = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum
'''


def cambiar_texto():
    return 'cambio'


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        self.source = './src/img/{0}_128_GrayBack.png'.format(self.custom)

    def on_release(self):
        self.source = './src/img/{0}_128.png'.format(self.custom)


# class HeaderWidget(Widget):
#     def __init__(self, **kwargs):
#         super(HeaderWidget, self).__init__(**kwargs)
#
#         with self.canvas:
#             Color(1, 0, 0, 1)  # set the colour to red
#             self.rect = Rectangle(pos=self.pos,
#                                   size=(self.width / 2.,
#                                         self.height / 2.))

class SettingsScreen(Screen):
    connct_btn_state = StringProperty('normal')
    log_text = StringProperty() # al cambiar el valor de esta propiedad no se actualizan sus referencias

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.log_text = mytext
        self.add_widget(self.build_settings_Screen())

    def build_settings_Screen(self):
        global log_text
        boxlayout = BoxLayout(orientation='vertical', padding=[10, 10, 10, 6])

        lyt_form = GridLayout(cols=1, size_hint=(1, .20), padding=[0, 0, 0, 10])
        btn2 = ToggleButton(text='Connect Raspberry', background_color=(.7, .7, 1, 1))
        btn2.bind(on_release=self.sniff_rpi)
        lyt_form.add_widget(btn2)

        # Log section
        lyt_log = GridLayout(cols=1, size_hint=(1, .76), padding=[0, 0, 0, 10])

        boxlayout_log = BoxLayout(orientation='vertical', size_hint=(1, .05))
        btn2 = Button(text='Refresh', size_hint=(.1, 1))
        boxlayout_log.add_widget(btn2)

        log = ScrollView(size_hint=(1, .95))
        label = TextInput(text=self.log_text, multiline=True)
        log.add_widget(label)

        lyt_log.add_widget(boxlayout_log)
        lyt_log.add_widget(log)
        # Log section End

        lyt_footer = GridLayout(cols=1, size_hint=(1, .04))
        btn_back = Button(text='Back')
        btn_back.bind(on_release=self.back_to_main)
        lyt_footer.add_widget(btn_back)

        boxlayout.add_widget(lyt_form)
        boxlayout.add_widget(lyt_log)
        boxlayout.add_widget(lyt_footer)
        return boxlayout

    def back_to_main(self, *args):
        self.parent.current = 'menu'

    def sniff_rpi(self, *args):
        # time.sleep(2)
        print(self.log_text)
        # self.log_text = 'test'
        args[0].state = 'normal'
        args[0].text = 'Disconnect Raspberry'
        args[0].background_color = (1, 1, 1, 1)