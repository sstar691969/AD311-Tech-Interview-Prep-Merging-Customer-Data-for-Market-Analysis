# test_merge_customers.py
import unittest
from merge_customers import merge_customers

class TestMergeCustomers(unittest.TestCase):

    # Normal cases
    def test_normal_case_1(self):
        data1 = [101,104,107,0,0,0]
        data2 = [102,105,108]
        merge_customers(data1, 3, data2, 3)
        self.assertEqual(data1, [101,102,104,105,107,108])

    def test_normal_case_2(self):
        data1 = [1,3,5,0,0]
        data2 = [2,4]
        merge_customers(data1, 3, data2, 2)
        self.assertEqual(data1, [1,2,3,4,5])

    def test_normal_case_3(self):
        data1 = [10,20,0]
        data2 = [15]
        merge_customers(data1, 2, data2, 1)
        self.assertEqual(data1, [10,15,20])

    # Edge cases
    def test_edge_case_empty_data2(self):
        data1 = [103]
        data2 = []
        merge_customers(data1, 1, data2, 0)
        self.assertEqual(data1, [103])

    def test_edge_case_empty_data1(self):
        data1 = [0,0,0]
        data2 = [1,2,3]
        merge_customers(data1, 0, data2, 3)
        self.assertEqual(data1, [1,2,3])

    def test_edge_case_duplicates(self):
        data1 = [1,2,2,0,0,0]
        data2 = [2,3,4]
        merge_customers(data1, 3, data2, 3)
        self.assertEqual(data1, [1,2,2,2,3,4])

if __name__ == "__main__":
    unittest.main()
