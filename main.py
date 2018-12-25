import kivy
kivy.require('1.9.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.properties import StringProperty

import logging
import _thread

from  dronemodules.widgets import *
from dronemodules.controlloger import MyLabelHandler
from dronemodules.mqqsubscriber import MQTTSubscriber


ROWS = ['Goc', 'COC', 'EEE', 'abs' , 'kju' , 'iop' , 'nmg', 'gty', 'jkio', 'dbkgcd' , 'udbcbjkb']

# KV Files con las vistas de la app
Builder.load_file('kvFiles/settingscreen.kv')
Window.clearcolor = (1, 1, 1, 1)  # Esto es para colocar el fondo de la ventana de color blanco

MQQT_DISCONNECT = False
mqtt_subscriber = None


def my_thread(log):
    global mqtt_subscriber
    mqtt_subscriber = MQTTSubscriber(log)
    mqtt_subscriber.run()
    # while True:
    #    if MQQT_DISCONNECT:
    #        break
    # mqttsubscriber.disconnect()

    # for i in range(10):
    #    time.sleep(1)
    #    log.info("\nWOO %s", i)


class MenuScreen(Screen):
    counter = NumericProperty(0)

    def my_callback(self, button):
        print('The button ' + button + ' has been pushed')
        self.counter += 1


class SettingScreen(Screen):
    log_text = StringProperty('')

    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)
        # self.log_text = '[b][color=ff3333]Hello[/color][/b]'

    def do_test(self, texto):
        # LOGGERFIX: Crear un archivo de configuracion para el logger
        log = logging.getLogger("Control")
        log.level = logging.DEBUG
        # log.level = logging.INFO
        log.addHandler(MyLabelHandler(self.ids['f_but'], logging.DEBUG))

        _thread.start_new(my_thread, (log,))
        # self.log_text = cambiar_texto()
        print(texto)


class DroneControllerApp(App):
    def build(self):
        print("init")


if __name__ == '__main__':
    DroneControllerApp().run()
