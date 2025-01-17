
import unittest

from knapsack import knapsack as k


class Test(unittest.TestCase):
    def test_base_case(self):
        cap = 0
        val = [0]
        w = [0]
        c = len(val)
        assert k.knapsack(cap, w, val, c) == 0

        val = [60]
        w = [10]
        c = len(val)
        assert k.knapsack(cap, w, val, c) == 0

    def test_easy_case(self):
        cap = 3
        val = [1, 2, 3]
        w = [3, 2, 1]
        c = len(val)
        assert k.knapsack(cap, w, val, c) == 5

    def test_knapsack(self):
        cap = 50
        val = [60, 100, 120]
        w = [10, 20, 30]
        c = len(val)
        assert k.knapsack(cap, w, val, c) == 220


if __name__ == "__main__":
    unittest.main()
