import unittest

from NodeData import NodeData

class TestNodeData(unittest.TestCase):



    def test_Id(self):
        n1 = NodeData(1, (2.42,3.2323))
        id1 = n1.getId()
        self.assertEqual(id1, 1)

    def test_Get_Pos(self):
        n1 = NodeData(1, (34.23665, -2))
        pos1 = n1.getPos()
        self.assertEqual(pos1, (34.23665, -2))

    def test_Set_Pos(self):
        n1 = NodeData(1, (34.23665, -2))
        n1.setPos(1,2)
        self.assertEqual(n1.getPos(), (1, 2))



if __name__ == '__main__':
    unittest.main()