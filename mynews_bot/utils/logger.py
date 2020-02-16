import logging

def get_logger():

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    _logger.addHandler(ch)

    return _logger

logger = get_logger()