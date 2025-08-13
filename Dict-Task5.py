"""Find key with highest value 
   Task: Use max(dict, key=dict.get). 
   Input: {'a':5,'b':9} 
   Output: 'b' """
Dic={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 77, 'H': 88, 'I': 9, 'J': 10,'K':11}
max_key=max(Dic,key=Dic.get)
print(max_key)

