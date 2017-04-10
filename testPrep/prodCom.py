from threading import Thread, Condition
import time
import random

queue = []
MAX = 10
sp = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue

        while True:
            sp.acquire()

            if len(queue) == MAX:
                print("Queue full, producer is waiting")
                sp.wait()
                print("Space in queue, Consumer notified the producer")

            num = random.choice(nums)
            queue.append(num)
            print("Produced", queue)
            sp.notify()
            sp.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue

        while True:
            sp.acquire()

            if not queue:
                print("Nothing in queue, consumer is waiting")
                sp.wait()
                print("Producer added something to queue and notified the consumer")

            num = queue.pop(0)
            print("Consumed", num)
            sp.notify()
            sp.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()


