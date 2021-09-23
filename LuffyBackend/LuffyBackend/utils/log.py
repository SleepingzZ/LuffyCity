import logging


def get_logger(source='django'):
    return logging.getLogger(source)


logger = logging.getLogger('django')
