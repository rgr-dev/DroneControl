import kivy
kivy.require('1.9.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import *
from kivy.lang import Builder
from kivy.core.window import Window

import logging
import _thread

from  dronemodules.widgets import *
from dronemodules.controlloger import MyLabelHandler
from dronemodules.mqqsubscriber import MQTTSubscriber

# KV Files con las vistas de la app
Builder.load_file('kvFiles/settingscreen.kv')
Window.clearcolor = (1, 1, 1, 1)  # Esto es para colocar el fondo de la ventana de color blanco

MQQT_DISCONNECT = False
mqtt_subscriber = None
log = None


def connection_thread(logger, drone_ip, drone_port):
    global mqtt_subscriber
    if mqtt_subscriber is None:
        mqtt_subscriber = MQTTSubscriber(logger)
        mqtt_subscriber.run()
    else:
        mqtt_subscriber.fast_connection()


def disconnect_drone():
    global mqtt_subscriber
    mqtt_subscriber.disconnect()


class MenuScreen(Screen):
    counter = NumericProperty(0)

    def my_callback(self, button):
        print('The button ' + button + ' has been pushed')
        self.counter += 1


class SettingScreen(Screen):
    log_text = StringProperty('')

    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)

    def init_drone_connection(self, connect_btn, drone_ip, drone_port):
        global log
        btn_state = connect_btn.state
        if drone_ip and drone_port:
            if btn_state == 'down':
                # LOGGERFIX: Crear un archivo de configuracion para el logger
                if log is None:
                    log = logging.getLogger("Control")
                    log.level = logging.DEBUG
                    # log.level = logging.INFO
                    log.addHandler(MyLabelHandler(self.ids['log_box'], logging.DEBUG))

                _thread.start_new(connection_thread, (log, drone_ip, drone_port,))
                connect_btn.text = 'Disconnect'
                print('%s:%s', drone_ip, drone_port)
            elif btn_state == 'normal':
                disconnect_drone()
                connect_btn.text = 'Connect'


class DroneControllerApp(App):
    def build(self):
        print("init")


if __name__ == '__main__':
    DroneControllerApp().run()
