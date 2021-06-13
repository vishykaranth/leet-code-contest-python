import unittest

from Weekly.solutions.Weekly_Contest_245.Solution_1899 import Solution_1899


class TestSolution_1899(unittest.TestCase):
    def testHappyPath(self):
        s = Solution_1899()
        triplets = s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])
        self.assertEqual(triplets, True)

    def testHappyPath2(self):
        s = Solution_1899()
        triplets = s.mergeTriplets([[1, 3, 4], [2, 5, 8]], [2, 5, 8])
        self.assertEqual(triplets, True)

    def testHappyPath3(self):
        s = Solution_1899()
        triplets = s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])
        self.assertEqual(triplets, True)

    def testFalse(self):
        s = Solution_1899()
        triplets = s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5])
        self.assertEqual(triplets, False)


if __name__ == '__main__':
    unittest.main()
