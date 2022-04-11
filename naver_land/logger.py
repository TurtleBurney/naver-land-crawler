import logging


def init_logger():
    logger = logging.getLogger()

    if len(logger.handlers) > 0:
        return logger
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.setLevel(logging.INFO)
    return logger
