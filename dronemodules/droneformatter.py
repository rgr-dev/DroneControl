import logging


class DroneFormatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None, style='%'):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        message = super(DroneFormatter, self).format(record)
        if record.levelname == "DEBUG":
            message = "\n[color=#00c100]" + message.replace("DEBUG", "DEB", 1) + "[/color]"
        elif record.levelname == "INFO":
            message = "\n[color=#000000]" + message.replace("INFO", "INF", 1) + "[/color]"
        elif record.levelname == "WARNING":
            message = "\n[color=ff3333]" + message.replace("WARNING", "WAR", 1) + "[/color]"
        elif record.levelname == "ERROR":
            message = "\n[color=ff3333]" + message.replace("ERROR", "ERR", 1) + "[/color]"
        elif record.levelname == "CRITICAL":
            message = "\n[color=ff3333]" + message.replace("CRITICAL", "CRI", 1) + "[/color]"
        return message
