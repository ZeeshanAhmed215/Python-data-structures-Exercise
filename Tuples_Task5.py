"""Count occurrences of a value 
   Task: Use .count() method. 
   Input: (1,2,2,3) 
   Output: 2 """

tup=(1,2,2,3,3,4,4,5,5,5,6,)
input_int=int(input("Enter your number::} "))
count_num=tup.count(input_int)
print(f"{input_int} is {count_num} times in this tupple.")