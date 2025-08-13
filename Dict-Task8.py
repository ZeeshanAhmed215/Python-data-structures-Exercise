""" Check if value exists in dictionary 
    Task: Use in with .values() method. 
    Input: 2 in {'a':1,'b':2} 
    Output: True """
input_num=3
Dic={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
if input_num in Dic.values():
    print("True")
else:
    print("False")