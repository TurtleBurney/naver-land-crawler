import time
import structlog
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()
logger = structlog.get_logger()


def run():
    sched.add_job(job1, 'cron', second='*/2', id="test_1")
    sched.add_job(job2, 'cron', second='*/3', id="test_2")
    sched.add_job(job3, 'cron', second='*/5', id="test_3")
    sched.start()


def job1():
    print('hio')
    # logger.info(f'  job1 : 2 초 마다 실행  {time.strftime("%H:%M:%S")}')


def job2():
    logger.info(f'  job2 : 3 초 마다 실행  {time.strftime("%H:%M:%S")}')


def job3():
    logger.info(f'  job3 : 5 초 마다 실행  {time.strftime("%H:%M:%S")}')
