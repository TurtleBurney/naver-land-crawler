import time
import structlog
from app.run import run
from app.utils.logger import init_logger
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()
logger = structlog.get_logger()


if __name__ == "__main__":
    init_logger()
    logger.info(f'Scheduling Start {time.strftime("%H:%M:%S")}')
    sched.start()

    while True:
        try:
            run(scheduler=sched)

            time.sleep(1000)
        except KeyboardInterrupt:
            logger.warn("Abort !!")
            break

    sched.shutdown()
    logger.info(f'Scheduling done  {time.strftime("%H:%M:%S")}')
