
import unittest
from Algorithms.bubble_sort import bubble



class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.bubble_sort = bubble()

    def test_sorted_array(self):

        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        result = self.bubble_sort.bubble_sort(array)

        self.assertEqual(result, [1, 3, 8, 9, 10, 12, 13, 23, 24, 41])


    def test_graph_generation_is_correct(self):

        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        self.bubble_sort.bubble_sort(array)

        val = len(self.bubble_sort.arr)

        self.assertEqual(val,1)





if __name__ == '__main__':
    unittest.main()
