import random
import nsq
import tornado.ioloop

# send a random integer to `numbers`
def pub_message():
    msg = str(random.randint(1, 99999))
    writer.pub('numbers', msg, finish_pub)

# print what we sent
def finish_pub(conn, data):
    print("Data published to queue")

writer = nsq.Writer(['127.0.0.1:4150'])
# run `pub_message` every second
tornado.ioloop.PeriodicCallback(pub_message, 100).start()
nsq.run()
