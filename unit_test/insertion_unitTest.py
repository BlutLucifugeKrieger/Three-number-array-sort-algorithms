
import unittest
from Algorithms.insertion_sort import insertion



class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.insertion_sort = insertion()

    def test_sorted_array(self):

        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        result = self.insertion_sort.insertion_sort(array)

        self.assertEqual(result, [1, 3, 8, 9, 10, 12, 13, 23, 24, 41])


    def test_graph_generation_is_correct(self):

        array = [1, 3, 10, 8, 9, 12, 23, 41, 13, 24]

        self.insertion_sort.insertion_sort(array)

        val = len(self.insertion_sort.arr)

        self.assertEqual(val,1)





if __name__ == '__main__':
    unittest.main()
