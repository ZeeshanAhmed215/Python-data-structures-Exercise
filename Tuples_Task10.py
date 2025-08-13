"""  Zip and unzip lists to tuples 
     Task: Use zip() to combine and *zip to unzip. 
     Input: [1,2], ['a','b'] 
     Output: [(1,'a'),(2,'b')] """

num_list=[1,2,3,4,5]
Char_list=['A', 'B', 'C', 'D', 'E']
Final_list=[]
for num,char in zip(num_list,Char_list):
    tup=(num,char)
    Final_list.append(tup)
print(Final_list)