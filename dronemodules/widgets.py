from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


def cambiar_texto():
    return 'cambio'


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        self.source = './src/img/{0}_128_GrayBack.png'.format(self.custom)

    def on_release(self):
        self.source = './src/img/{0}_128.png'.format(self.custom)
