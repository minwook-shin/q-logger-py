import logging
import queue


class QueueHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_queue = queue.Queue(-1)

    def emit(self, record):
        self.log_queue.put(record)
