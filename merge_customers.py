
# merge_customers.py

from typing import List

def merge_customers(customerData1: List[int], m: int, customerData2: List[int], n: int) -> None:
    """
    Merges customerData2 into customerData1 in-place.
    """
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    # Merge from the end
    while p1 >= 0 and p2 >= 0:
        if customerData1[p1] > customerData2[p2]:
            customerData1[p] = customerData1[p1]
            p1 -= 1
        else:
            customerData1[p] = customerData2[p2]
            p2 -= 1
        p -= 1
    
    # Copy remaining elements from customerData2
    while p2 >= 0:
        customerData1[p] = customerData2[p2]
        p2 -= 1
        p -= 1


if __name__ == "__main__":
    # Example input
    data1 = [101, 104, 107, 0, 0, 0]
    data2 = [102, 105, 108]
    merge_customers(data1, 3, data2, 3)
    
    print("Merged customer data:", data1)
