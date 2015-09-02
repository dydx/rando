import nsq
from math import sqrt
from itertools import count, islice

def primep(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if not n % number:
            return False
    return True

def handler(message):
    number = int(message.body)
    if primep(number):
        print "Prime"
    else:
        print "Not-Prime"
    return True

reader = nsq.Reader(
        lookupd_http_addresses = ['http://127.0.0.1:4161'],
        message_handler = handler,
        topic = 'numbers',
        channel = 'primes',
)

nsq.run()
