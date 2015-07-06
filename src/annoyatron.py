import random
import time
import functools
import decorator
import winsound

DEBUG = False

def sleep(min=2, max=25):
    sleep_time = random.randrange(min, max)
    if DEBUG:
        print('will beep in {} sec'.format(sleep_time))
    else:
        sleep_time *= 60
    time.sleep(sleep_time)

@decorator.decorator
def sleepify(func, *args, **kw):
    sleep()
    return func(*args, **kw)

@sleepify
def annoyatron():
    frequency = random.randrange(37, 32768)
    #avoid inautable sounds
    while 17037 < frequency < 29037:
        frequency = random.randrange(37, 32768)
    interval = random.randrange(50, 800)
    winsound.Beep(frequency, interval)

while True:
    annoyatron()