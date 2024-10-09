import logging
from logging.handlers import TimedRotatingFileHandler


class _log:
    def __init__(self,log_name):

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)

        file_handler = TimedRotatingFileHandler("./"+log_name+".log", when='midnight', interval=1, backupCount=7)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)


    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        
        self.logger.critical(message)



if __name__ == "__main__":
    ml = _log("test")
    ml.info("test")
