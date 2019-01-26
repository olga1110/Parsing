import logging
import logging.handlers


# logger = None
# log_client = None


def log_parse_init():

    # global logger
    logger = logging.getLogger("excel_parse")
    logger_file_name = 'excel_parse.log'
    fn = logging.handlers.TimedRotatingFileHandler(logger_file_name, when='D',
                                            interval=1,
                                            backupCount=31)

    fn.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    fn.setFormatter(formatter)

    logger.addHandler(fn)
    logger.setLevel(logging.ERROR)
    return logger
