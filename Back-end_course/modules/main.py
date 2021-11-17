# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import datetime
import sys
import greet


def wait(seconds):
    time.sleep(seconds)


def my_sin(f):
    return math.sin(f)


def iso_now():
    return datetime.datetime()


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return greet.supergreeting(name)
