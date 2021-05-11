import unittest
from main import determinant
from main import get_inverse_matrix
from main import multiply_by_vector
from main import get_unknown_members



class TestMethods(unittest.TestCase):

    def test_det1(self):
        self.assertEqual(determinant([[1, 2], [3, 4]]), -2)

    def test_det2(self):
        self.assertEqual(determinant([[6, 1], [4, 1]]), 2)

    def test_det3(self):
        self.assertEqual(determinant([[1, -1, 3], [2, 6, 1], [-1, 4, 1]]), 47)

    def test_inverse1(self):
        self.assertEqual(get_inverse_matrix([[1, 2], [3, 4]]), [[-2, 1], [1.5, -0.5]])

    def test_inverse2(self):
        self.assertEqual(get_inverse_matrix([[1, 0, 0], [1, -1, 0], [1, 0, 1]]), [[1, 0, 0], [1, -1, 0], [-1, 0, 1]])

    def test_inverse3(self):
        self.assertEqual(get_inverse_matrix([[2, 3, 1], [3, 4, 2], [1, 1, 2]]), [[-6, 5, -2], [4, -3, 1], [1, -1, 1]])

    def test_multyply1(self):
        self.assertEqual(multiply_by_vector([[1, 2, 3], [6, 5, 4], [7, 8, 9]], [1, 1, 1]), [6, 15, 24])

    def test_multyply2(self):
        self.assertEqual(multiply_by_vector([[3, -1, 2], [4, 2, 0], [-5, 6, 1]], [8, 7, 2]), [21, 46, 4])

    def test_members1(self):
        self.assertEqual(get_unknown_members([[1, -1], [1, 1]], [1, 3]), [2, 1])

    def test_members2(self):
        self.assertEqual(get_unknown_members([[3, 2, 1], [2, 3, 1], [2, 1, 3]], [5, 1, 11]), [2, -2, 3])


if __name__ == '__main__':
    unittest.main()
