import logging

from q_logger_py import QueueHandler, ThreadStdoutWorker, ThreadRotateFileWorker

queue_handler = QueueHandler()
thread_worker = ThreadStdoutWorker(queue_handler.log_queue)

logger = logging.getLogger(__name__)
logger.addHandler(queue_handler)
logger.setLevel(logging.DEBUG)

thread_worker.start()
logger.debug('This is a debug')
logger.info('This is a info')
logger.warning('This is a warning')
logger.error('This is an error')
thread_worker.end()

thread_worker = ThreadRotateFileWorker(queue_handler.log_queue, 'test.log')
logger.addHandler(queue_handler)

thread_worker.start()
logger.debug('This is a debug')
logger.info('This is a info')
logger.warning('This is a warning')
logger.error('This is an error')
thread_worker.end()
