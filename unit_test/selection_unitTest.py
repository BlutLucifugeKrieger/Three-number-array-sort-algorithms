import unittest
from Algorithms.selection_sort import selection


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.selection_sort = selection()

    def test_selection_array(self):
        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        result = self.selection_sort.selection_sort(array)

        self.assertEqual(result, [1, 3, 8, 9, 10, 12, 13, 23, 24, 41])

    def test_graph_generation_is_correct(self):
        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        self.selection_sort.selection_sort(array)

        val = len(self.selection_sort.arr)

        self.assertEqual(val, 1)


if __name__ == '__main__':
    unittest.main()
