"""Create dict from two lists 
   Task: Use zip(keys, values) and dict(). 
   Input: ['a','b'], [1,2] 
   Output: {'a':1,'b':2} """

Alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Dic={}
for x,y in zip(Alpha_list,Num_list):
    Dic[x]=y

print(Dic)