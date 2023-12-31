from threading import Thread
from time import sleep


class Hello(Thread):

    def run(self):
       for i in range(10):
            print("Hello")
            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()


t1.start()
sleep(0.2)
t2.start()

#this how asking to main thread wait untill this thread complete
t1.join()
t2.join()

print("bye")

