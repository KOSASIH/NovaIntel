import logging

class Logger:
    def __init__(self, log_level):
        self.log_level = log_level
        self.logger = logging.getLogger('NovaIntel')
        self.logger.setLevel(log_level)

    def log(self, message):
        self.logger.log(self.log_level, message)
