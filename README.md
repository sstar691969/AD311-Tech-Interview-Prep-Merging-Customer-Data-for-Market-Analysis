# AD311-Tech-Interview-Prep-Merging-Customer-Data-for-Market-Analysis


Merging Customer Data


William Anderson

AD311

Normal Cases

[101,104,107,0,0,0] + [102,105,108]

[1,3,5,0,0] + [2,4]

[10,20,0] + [15]

Edge Cases

data2 = []

data1 = [0,0,0], m = 0

Duplicate IDs [1,2,2,0,0,0] + [2,3,4]


Complexity to Mention

Time Complexity: O(m + n)

Space Complexity: O(1) (in-place merge).


            ┌───────────────┐
            │     Start     │
            └───────┬───────┘
                    │
                    ▼
        ┌──────────────────────────┐
        │ Input arrays + m and n   │
        └──────────┬───────────────┘
                   │
                   ▼
     ┌────────────────────────────────┐
     │ Initialize pointers:           │
     │ p1 = m-1, p2 = n-1, p = m+n-1  │
     └──────────────┬─────────────────┘
                    │
                    ▼
        ┌─────────────────────────────┐
        │ While p1 >= 0 AND p2 >= 0   │
        └──────────────┬──────────────┘
                       │
                       ▼
        ┌─────────────────────────────┐
        │ Compare customerData1[p1]   │
        │ and customerData2[p2]       │
        └──────────────┬──────────────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
┌───────────────────┐     ┌───────────────────┐
│ data1[p1] > data2 │     │ data2 >= data1    │
│ Place data1[p1]   │     │ Place data2[p2]   │
│ at index p        │     │ at index p        │
└───────┬───────────┘     └───────┬───────────┘
        │                           │
        ▼                           ▼
   p1-- and p--                p2-- and p--
        │                           │
        └─────────────┬─────────────┘
                      ▼
            (repeat while loop)

                    ▼
     ┌─────────────────────────────────┐
     │ Copy remaining elements from    │
     │ customerData2 if p2 >= 0        │
     └──────────────┬──────────────────┘
                    │
                    ▼
        ┌─────────────────────────────┐
        │  Merged array in data1      │
        └──────────────┬──────────────┘
                       │
                       ▼
                ┌───────────┐
                │    End    │
                └───────────┘
