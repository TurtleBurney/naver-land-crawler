import time
import structlog
from app.run import run
from app.utils.logger import init_logger


logger = structlog.get_logger()


if __name__ == '__main__':
    init_logger()
    logger.info(f'Scheduling Start {time.strftime("%H:%M:%S")}')

    while True:
        try:
            run()
            time.sleep(1000)
        except KeyboardInterrupt:
            logger.warn("Abort !!")
            break

    logger.info(f'Scheduling done  {time.strftime("%H:%M:%S")}')
