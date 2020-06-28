import time


print('Press Enter to begin, Press Ctrl + C to stop')

while True:
    try:
        input()
        start_time = time.time()
        print('Started')
        while True:
            print('Current Time :',time.strftime('%c',time.localtime()), '-', 'Time Elapsed :',round(time.time() - start_time, 0),'secs', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopped')
        end_time = time.time()
        print('Total time :',round(end_time - start_time,2),'secs')
        break
