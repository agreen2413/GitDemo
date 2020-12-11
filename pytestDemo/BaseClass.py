import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger





# import inspect
# import logging
#
# class BaseClass:
#     def getLogger(self):
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
#         logger = logging.getLogger(__name__)  #It will print your filename etc test_logging.py
#
#         filehandler = logging.FileHandler('logfile.log')  #Give it a log file name
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)") #result will be timestamp : warning/error/critical : name of the file etc test_logging.py : message e.g "An error has occured!
#         filehandler.setFormatter(formatter)
#
#         logger.addHandler(filehandler) #You will pass a fileHandler to this method
#         logger.setLevel(logging.INFO)
#         logger.debug("Debug statement is being executed!")    #These are the order of level..Debug, Info, Warning, Error and Critical
#         logger.info("Information statement but not related to any error!")
#         logger.warning("Something is in warning mode!")
#         logger.error("A major error has happened!")
#         logger.critical("A critical error has happened!")
