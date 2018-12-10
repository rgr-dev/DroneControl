from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

mytext = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum
'''


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        self.source = './src/img/{0}_128_GrayBack.png'.format(self.custom)

    def on_release(self):
        self.source = './src/img/{0}_128.png'.format(self.custom)


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.add_widget(self.build_settings_Screen())

    def build_settings_Screen(self):
        boxlayout = BoxLayout(orientation='vertical', padding=[10, 10, 10, 10])

        lyt_form = GridLayout(cols=1, size_hint=(1, .20))
        btn2 = Button(text='World')
        lyt_form.add_widget(btn2)

        lyt_log = GridLayout(cols=1, size_hint=(1, .76))
        btn2 = Button(text='World', size_hint=(.2, 1))
        log = ScrollView()
        label = Label(text=mytext, color=[0,0,0,1], halign='left')
        log.add_widget(label)
        lyt_log.add_widget(btn2)
        lyt_log.add_widget(log)

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