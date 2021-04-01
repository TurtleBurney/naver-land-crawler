import time
import structlog
from app.run import run
from app.utils.logger import init_logger
from apscheduler.schedulers.background import BackgroundScheduler
from data.config import load_config
from dotenv import find_dotenv, load_dotenv

sched = BackgroundScheduler()
logger = structlog.get_logger()

try:
    env_file = find_dotenv(".env", raise_error_if_not_found=True)
    load_dotenv(env_file, override=False)
except IOError:
    sample_env_file = find_dotenv(".env.sample", raise_error_if_not_found=True)
    load_dotenv(sample_env_file, override=False)


if __name__ == "__main__":
    config = load_config()
    init_logger()
    logger.info(f'Scheduling Start {time.strftime("%H:%M:%S")}')
    sched.start()

    while True:
        try:
            run(scheduler=sched, config=config)

            time.sleep(1000)
        except KeyboardInterrupt:
            logger.warn("Abort !!")
            break

    sched.shutdown()
    logger.info(f'Scheduling done  {time.strftime("%H:%M:%S")}')
