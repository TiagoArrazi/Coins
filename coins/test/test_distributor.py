import unittest
from src.utils.coint_distributor import Distributor


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
        self.assertEqual(Distributor.distribute(2.55), mock_1)

    def test_case_2(self):
        self.assertEqual(Distributor.distribute(50.49), mock_2)

    def test_case_3(self):
        self.assertEqual(Distributor.distribute(20.99), mock_3)
