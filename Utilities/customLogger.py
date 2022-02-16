import logging

class Log:

    @staticmethod
    def loggen():

        logging.basicConfig(filename="D:\python Q\e-commerce\logs\\automaation.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %H:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger