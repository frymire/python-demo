import threading
import time


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads (or comment it out to experiment).
        thread_lock.acquire()
        self.print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        thread_lock.release()

    def print_time(self, thread_name, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (thread_name, time.ctime(time.time())))
            counter -= 1


thread_lock = threading.Lock()
threads = []

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
