import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import product_service

class TestProductService(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
