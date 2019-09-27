import unittest

mock_1 = {1.0: 2,
          0.5: 1,
          0.25: 0,
          0.1: 0,
          0.05: 1,
          0.01: 0}

mock_2 = {1.0: 50,
          0.5: 0,
          0.25: 1,
          0.1: 2,
          0.05: 0,
          0.01: 4}

mock_3 = {1.0: 20,
          0.5: 1,
          0.25: 1,
          0.1: 2,
          0.05: 0,
          0.01: 4}


class TestDistributor(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual()