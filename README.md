# q-logger-py

**q-logger-py** is a pure Python 3 logging library that use queues for handling log messages. 

It is thread-based, which makes it faster than standard file logging.

![](https://github.com/minwook-shin/q-logger-py/blob/main/speed_benchmark_figure.png?raw=true)

## Installation

```bash
pip install q-logger-py
```

## Usage

first need to create a `QueueHandler` and a `ThreadWorker` (either `ThreadStdoutWorker` or `ThreadRotateFileWorker`). 

Then, add the `QueueHandler` to your logger and start the `ThreadWorker`.

```python
import logging
from q_logger_py import QueueHandler, ThreadStdoutWorker

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
```

## Features

- **Thread-based**: uses threads to handle log messages, which makes it faster than standard file logging.
- **Queue-based**: uses queues to store log messages, which ensures that no log messages are lost.

## Custom Output

key features of q-logger-py is the ease of creating custom outputs. 

By inheriting from the `BaseThreadWorker` class, you can define `output` method to handle records in any way you want. 

```python
from q_logger_py.worker.base_thread_worker import BaseThreadWorker

class ThreadFileWorker(BaseThreadWorker):
    def __init__(self, log_queue, filename):
        super().__init__(log_queue)
        self.file = open(filename, 'a')

    def output(self):
        log_output = self.format(self.record)
        # add custom output here
        # self.file.write(log_output + '\n')
        # self.file.flush()
        print(log_output)
```

## License

q-logger-py is licensed under the Apache License.

## Project Links

- [Homepage](https://github.com/minwook-shin/q-logger-py)
- [Bug Tracker](https://github.com/minwook-shin/q-logger-py/issues)
