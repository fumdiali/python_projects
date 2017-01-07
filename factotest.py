#unit test for facto.py

import unittest
from facto import fact_num

class FactoTestCase(unittest.TestCase):

  def test_facto_of_99(self):
      self.assertTrue(fact_num(99))

if __name__ == '__main__':
  unittest.main()
