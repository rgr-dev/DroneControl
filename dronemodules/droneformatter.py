import logging


class DroneFormatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None, style='%'):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        message = super(DroneFormatter, self).format(record)
        if record.levelname == "DEBUG":
            message = "\n[color=#00c100]" + message + "[/color]"
        elif record.levelname == "INFO":
            message = "\n[color=#000000]" + message + "[/color]"
        elif record.levelname == "WARNING":
            message = "\n[color=ff3333]" + message + "[/color]"
        elif record.levelname == "ERROR":
            message = "\n[color=ff3333]" + message + "[/color]"
        elif record.levelname == "CRITICAL":
            message = "\n[color=ff3333]" + message + "[/color]"
        return message
