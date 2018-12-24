from kivy.clock import Clock
import logging


class MyLabelHandler(logging.Handler):

    def __init__(self, logger_box, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        self.logger_box = logger_box

    def emit(self, record):
        """using the Clock module for thread safety with kivy's main loop"""

        def f(dt=None):
            self.logger_box.text += self.format(record)  # "use += to append..."

        Clock.schedule_once(f)
