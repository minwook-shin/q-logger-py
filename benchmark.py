import logging
import timeit
from logging.handlers import RotatingFileHandler

import matplotlib.pyplot as plt

from q_logger_py import QueueHandler, ThreadRotateFileWorker

queue_handler = QueueHandler()
thread_worker = ThreadRotateFileWorker(queue_handler.log_queue, 'q_logger.log')
logger_q = logging.getLogger('q_logger')
logger_q.addHandler(queue_handler)
logger_q.setLevel(logging.DEBUG)

file_handler = RotatingFileHandler('std_logger.log', maxBytes=50000, backupCount=5)
logger_std = logging.getLogger('std_logger')
logger_std.addHandler(file_handler)
logger_std.setLevel(logging.DEBUG)

iterations = range(10000, 100001, 10000)

times_q = []
times_std = []

for i in iterations:
    start_time = timeit.default_timer()
    thread_worker.start()
    for _ in range(i):
        logger_q.debug('This is a debug')
    thread_worker.end()
    times_q.append(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    for _ in range(i):
        logger_std.debug('This is a debug')
    times_std.append(timeit.default_timer() - start_time)

plt.title('File Logging performance')
plt.plot(iterations, times_q, label='q-logger-py : ThreadRotateFileWorker')
plt.plot(iterations, times_std, label='Standard logging : RotatingFileHandler')
plt.xlabel('Number of log messages')
plt.ylabel('Time (seconds)')
plt.text = "maxBytes=50000, backupCount=5"
plt.legend()
plt.show()
