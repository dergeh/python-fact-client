from factclient.fact import Fact, Provider

import unittest
import os
from factclient.trace_pb2 import Trace
from unittest.mock import patch


# TODO implement proper tests
class TestFact(unittest.TestCase):
    def test_read_file(self):
        pass

    def test_fingerprint(self):
        pass

    def test_boot(self):
        pass

    def test_send(self):
        pass

    def test_now(self):
        pass

    def test_load(self):
        pass

    def test_start(self):
        pass

    def test_update(self):
        pass

    def test_done(self):
        pass

    def test_set_parent_id(self):
        test_id = "test_id"
        Fact.set_parent_id(test_id)
        self.assertEqual(test_id, Fact._trace.ChildOf)


class TestFingerprint(unittest.TestCase):
    def test_aws_fingerprint(self):
        pass
    # os.environ["AWS_LAMBDA_LOG_STREAM_NAME"] = "test"

    # with patch('factclient.provider.AWSFact') as mock:
    #   trace = Trace()
    #  Fact.fingerprint(trace, None)
    # self.assertEqual(Fact._provider, Provider.AWS)


if __name__ == '__main__':
    unittest.main()
