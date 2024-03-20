import logging
import threading


class BaseThreadWorker:
    def __init__(self, log_queue):
        self.log_queue = log_queue
        self.worker_thread = None
        self.record = None
        self.formatter = logging.Formatter('%(levelname)s - %(message)s')

    def output(self):
        raise NotImplementedError('output must be implemented by ThreadWorker subclasses')

    def worker(self):
        while True:
            self.record = self.log_queue.get()
            if self.record is None:
                break
            self.output()

    def start(self):
        self.worker_thread = threading.Thread(target=self.worker)
        self.worker_thread.start()

    def end(self):
        self.log_queue.put(None)
        self.worker_thread.join()

    def format(self, record):
        return self.formatter.format(record)
