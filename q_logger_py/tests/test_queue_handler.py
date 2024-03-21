import unittest
from unittest.mock import Mock

from q_logger_py.handler.queue_handler import QueueHandler


class TestQueueHandler(unittest.TestCase):
    def setUp(self):
        self.queue_handler = QueueHandler()

    def test_emit_puts_record_in_queue(self):
        mock_record = Mock()
        self.queue_handler.emit(mock_record)
        self.assertEqual(self.queue_handler.log_queue.get(), mock_record)

    def test_emit_handles_multiple_records(self):
        mock_records = [Mock(), Mock(), Mock()]
        for record in mock_records:
            self.queue_handler.emit(record)
        for record in mock_records:
            self.assertEqual(self.queue_handler.log_queue.get(), record)

    def test_emit_queue_is_empty_after_all_records_are_consumed(self):
        mock_records = [Mock(), Mock(), Mock()]
        for record in mock_records:
            self.queue_handler.emit(record)
        while not self.queue_handler.log_queue.empty():
            self.queue_handler.log_queue.get()
        self.assertTrue(self.queue_handler.log_queue.empty())
