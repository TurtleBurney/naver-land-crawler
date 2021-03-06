import time
import structlog

logger = structlog.get_logger()


def run(scheduler):
    scheduler.add_job(job1, "cron", second="*/6", id="test_1")
    scheduler.add_job(job2, "cron", second="*/12", id="test_2")
    scheduler.add_job(job3, "cron", second="*/15", id="test_3")


def job1():
    logger.info(f' job1 :  3 초 마다 실행  {time.strftime("%H:%M:%S")}')


def job2():
    logger.info(f' job2 : 12 초 마다 실행  {time.strftime("%H:%M:%S")}')


def job3():
    logger.info(f' job3 : 15 초 마다 실행  {time.strftime("%H:%M:%S")}')
