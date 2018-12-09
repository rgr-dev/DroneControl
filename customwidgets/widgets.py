from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.uix.screenmanager import Screen


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        self.source = './src/img/{0}_128_GrayBack.png'.format(self.custom)

    def on_release(self):
        self.source = './src/img/{0}_128.png'.format(self.custom)


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        boxlayout = BoxLayout()
        boxlayout.add_widget(Button(text='My settings button'))
        back_button = Button(text='Back to menu')
        back_button.bind(on_press=self.back_to_main)
        boxlayout.add_widget(back_button)
        self.add_widget(boxlayout)

    def back_to_main(self, *args):
        self.parent.current = 'menu'