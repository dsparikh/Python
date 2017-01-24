import threading

class Mesenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = Mesenger(name="Send")
y= Mesenger(name="Receive")
x.start()
y.start()
