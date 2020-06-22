import logging
import logging.handlers


class myLogger():
    def __init__(self, logger_name, log_level=logging.DEBUG, file_log=False, file_name='log.txt'):        
        # declare logger instance
        self.logger = logging.getLogger(logger_name)

        # declare formatter
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] ::: %(message)s')

        # declare handler
        streamHandler = logging.StreamHandler()
        if file_log: fileHandler = logging.FileHandler(file_name)

        # set formatter to instance
        streamHandler.setFormatter(formatter)
        if file_log: fileHandler.setFormatter(formatter)

        # set handler to logger
        self.logger.addHandler(streamHandler)
        if file_log: self.logger.addHandler(fileHandler)

        # set default log level
        self.logger.setLevel(log_level)


    def setLogger(self):
        return self.logger
