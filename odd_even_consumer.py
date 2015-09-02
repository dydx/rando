import nsq

def evenp(number):
    return number % 2 == 0

def handler(message):
    number = int(message.body)
    if evenp(number):
        print "Even"
    else:
        print "Odd"
    return True

reader = nsq.Reader(
        lookupd_http_addresses = ['http://127.0.0.1:4161'],
        message_handler = handler,
        topic = 'numbers',
        channel = 'odd_even',
)

nsq.run()
