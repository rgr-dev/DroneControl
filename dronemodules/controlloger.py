from dronemodules.droneformatter import DroneFormatter

from kivy.clock import Clock
import logging


class MyLabelHandler(logging.Handler):

    def __init__(self, logger_box, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        self.logger_box = logger_box
        # LOGGERFIX: Colocar este formatter en el archivo de configuracion del logger
        drone_formatter = DroneFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                         datefmt='%Y/%m/%d %H:%M:%S %p')
        self.setFormatter(drone_formatter)

    def emit(self, record):
        """using the Clock module for thread safety with kivy's main loop"""

        def f(dt=None):
            self.logger_box.text += self.format(record)

        Clock.schedule_once(f)
