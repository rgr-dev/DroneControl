import kivy
kivy.require('1.9.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # Esto es para colocar el fondo de la ventana de color blanco


class MenuScreen(Screen):
    counter = NumericProperty(0)

    def my_callback(self, button):
        print('The button ' + button + ' has been pushed')
        self.counter += 1


class SettingsScreen(Screen):
    pass


class DroneControllerApp(App):
    def build(self):
        print("init")


if __name__ == '__main__':
    DroneControllerApp().run()
