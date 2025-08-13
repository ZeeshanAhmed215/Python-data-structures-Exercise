""" Invert dictionary (value as key) 
    Task: Swap keys and values. 
    Input: {'a':1,'b':2} 
    Output: {1:'a', 2:'b'} """
Dic={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
Dic2={}
key_list=[]
value_list=[]
for x in Dic.keys():
    key_list.append(x)
for y in Dic.values():
    value_list.append(y)

for x,y in zip(value_list,key_list):
       Dic2[x]=y

print(Dic)
print(Dic2)