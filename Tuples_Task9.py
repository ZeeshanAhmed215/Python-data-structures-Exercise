"""  Take input and convert to tuple 
     Task: Split input string by comma and convert to integers. 
     Input: "1,2,3" 
     Output: (1,2,3) """
input_string="1,2,3,4,5,6,7,8,9,10"
split_string=input_string.split(",")
list_=[]
for i in split_string:
    list_.append(i)
tup=tuple(list_)
print(tup)