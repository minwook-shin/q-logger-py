import sys

from q_logger_py.worker.base_thread_worker import BaseThreadWorker


class ThreadStdoutWorker(BaseThreadWorker):
    def __init__(self, log_queue):
        super().__init__(log_queue)

    def output(self):
        log_output = self.format(self.record)
        sys.stdout.write(log_output + '\n')
