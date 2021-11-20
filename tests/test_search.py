import unittest
import search

class TestSearch(unittest.TestCase):

    def test_binary_search_simple_recursive(self):
        self.assertEqual(search.binary_search_simple_recursive([1], 1), 0)
        self.assertEqual(search.binary_search_simple_recursive([], 1), 0)
        self.assertEqual(search.binary_search_simple_recursive([2], 1), 0)
        self.assertEqual(search.binary_search_simple_recursive([1, 4, 5], 1), 0)
        self.assertEqual(search.binary_search_simple_recursive([1, 4, 5, 8], 4), 1)
        self.assertEqual(search.binary_search_simple_recursive([1, 4, 5, 8, 9, 12, 14], 12), 5)
        self.assertEqual(search.binary_search_simple_recursive([1, 4, 5, 8, 9, 12, 14], 13), 6)

    def test_binary_search_recursive(self):
        self.assertEqual(search.binary_search_recursive([1], 1), 0)
        self.assertEqual(search.binary_search_recursive([], 1), -1)
        self.assertEqual(search.binary_search_recursive([2], 1), -1)
        self.assertEqual(search.binary_search_recursive([1, 4, 5], 1), 0)
        self.assertEqual(search.binary_search_recursive([1, 4, 5, 8], 4), 1)
        self.assertEqual(search.binary_search_recursive([1, 4, 5, 8, 9, 12, 14], 12), 5)
        self.assertEqual(search.binary_search_recursive([1, 4, 5, 8, 9, 12, 14], 13), -1)

    def test_binary_search_iterative(self):
        self.assertEqual(search.binary_search_iterative([1], 1), 0)
        self.assertEqual(search.binary_search_iterative([], 1), -1)
        self.assertEqual(search.binary_search_iterative([2], 1), -1)
        self.assertEqual(search.binary_search_iterative([1, 4, 5], 1), 0)
        self.assertEqual(search.binary_search_iterative([1, 4, 5, 8], 4), 1)
        self.assertEqual(search.binary_search_iterative([1, 4, 5, 8, 9, 12, 14], 12), 5)
        self.assertEqual(search.binary_search_iterative([1, 4, 5, 8, 9, 12, 14], 13), -1)


if __name__ == '__main__':
    unittest.main()
