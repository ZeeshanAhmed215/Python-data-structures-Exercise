"""Filter even numbers 
    Task: Use list comprehension with condition x % 2 == 0. 
    Input: [1,2,3,4] 
   Output: [2,4] """

Num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
filter_list=[x for x in Num_list if x%2==0]
print(filter_list)