""" Flatten nested list 
Task: Use nested loops or list comprehension. 
Input: [[1,2],[3]] 
Output: [1,2,3]"""
num_list=[[1,2],[3,4],[4,6],[7,8],[9,10]]
num_list2=[i for x in num_list for i in x]
print(num_list,num_list2)