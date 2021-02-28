import time
from app.run import run


if __name__ == '__main__':
    while True:
        try:
            print(f'Scheduling Start {time.strftime("%H:%M:%S")}')
            run()
            print(f'Scheduling done  {time.strftime("%H:%M:%S")}')
        except KeyboardInterrupt:
            print("Abort !!")

        time.sleep(1000)
