import logging


logger = logging.getLogger(__name__)


# To ensure reload() doesn't add another one
if not logger.handlers:
    logger.addHandler(logging.NullHandler())


