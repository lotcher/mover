import logging
import colorlog
from functools import wraps


def check(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if Logger.logger is None:
            Logger.init()
        return func(*args, **kwargs)

    return decorator


class Logger:
    logger = None

    @classmethod
    def init(cls):
        handler = colorlog.StreamHandler()
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s][%(levelname)s] : %(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red'
            },
            reset=True
        )

        handler.setFormatter(formatter)
        logger = colorlog.getLogger('root')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        cls.logger = logger

    @classmethod
    @check
    def debug(cls, msg):
        cls.logger.debug(msg)

    @classmethod
    @check
    def info(cls, msg):
        cls.logger.info(msg)

    @classmethod
    @check
    def warning(cls, msg):
        cls.logger.warning(msg)

    @classmethod
    @check
    def error(cls, msg):
        cls.logger.error(msg)
