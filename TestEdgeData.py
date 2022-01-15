import unittest

from EdgeData import EdgeData

class TestEdgeData(unittest.TestCase):


    def test_get_src(self):
        e1 = EdgeData(2, 31 ,65.4334)
        self.assertEqual(e1.get_src(), 2)

    def test_get_dest(self):
        e1 = EdgeData(2, 31, 65.4334)
        self.assertEqual(e1.get_dest(), 31)

    def test_get_w(self):
        e1 = EdgeData(2, 31, 65.4334)
        self.assertEqual(e1.get_weight(), 65.4334)

if __name__ == '__main__':
    unittest.main()