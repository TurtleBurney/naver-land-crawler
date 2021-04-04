import time
import structlog
from app.crawler import NaverCrawler
from app.utils.logger import init_logger
from apscheduler.schedulers.background import BackgroundScheduler
from data.config import load_config
from dotenv import find_dotenv, load_dotenv

MODE = "DEBUG"
logger = structlog.get_logger()

try:
    env_file = find_dotenv(".env", raise_error_if_not_found=True)
    load_dotenv(env_file, override=False)
except IOError:
    sample_env_file = find_dotenv(".env.sample", raise_error_if_not_found=True)
    load_dotenv(sample_env_file, override=False)


class SchedulerLauncher(object):
    def __init__(self):
        self.config = load_config()
        self.scheduler = BackgroundScheduler()

    def launch(self):
        logger.info("Scheduling Start")
        self.scheduler.start()

        try:
            while True:
                try:
                    time.sleep(1000)
                except KeyboardInterrupt:
                    logger.warn("Abort !!")
                    break

        finally:
            logger.info("Scheduling done")
            self.scheduler.shutdown()

    def set_sched_task(self, task, name):
        self.scheduler.add_job(
            task, "interval", seconds=10, id=name, args=[self.config]
        )


if __name__ == "__main__":
    init_logger()

    if MODE == "DEBUG":
        crawler = NaverCrawler(load_config())
        crawler.run()
#    elif MODE == "SCHED":
#        launcher = SchedulerLauncher()
#        launcher.set_sched_task(crawler, "naver-crawler")
#        launcher.launch()
#    else:
#        logger.info(f"Mode {MODE} is not valid")
#
