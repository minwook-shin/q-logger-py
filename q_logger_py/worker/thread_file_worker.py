import logging
import os
import shutil

from q_logger_py.worker.base_thread_worker import BaseThreadWorker


class ThreadRotateFileWorker(BaseThreadWorker):
    def __init__(self, log_queue, filename, max_bytes=50000, backup_count=5, formatter=logging.Formatter()):
        super().__init__(log_queue, formatter)
        self.filename = filename
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.file = open(self.filename, 'a')

    def output(self):
        log_output = self.format(self.record)
        self.file.write(log_output + '\n')
        self.file.flush()

        if self.file.tell() > self.max_bytes:
            self.rotate()

    def rotate(self):
        self.file.close()
        for i in range(self.backup_count - 1, 0, -1):
            src = f"{self.filename}.{i}"
            dst = f"{self.filename}.{i + 1}"
            if os.path.exists(src):
                shutil.move(src, dst)
        shutil.move(self.filename, f"{self.filename}.1")
        self.file = open(self.filename, 'a')

    def __del__(self):
        self.file.close()
