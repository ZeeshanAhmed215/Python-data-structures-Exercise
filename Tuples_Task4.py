""" Find index of value 
    Task: Use .index() method. 
    Input: (1,2,3), value=2 
    Output: 1 """
Tup=(1,2,3,4,5,6,7,8,9,10)
print(f"{Tup}")
input_int=int(input("Enter your element::} "))
if input_int in Tup:
    print(f" Index of {input_int} is {Tup.index(input_int)}")
else:
    print(f"Invalid Input")