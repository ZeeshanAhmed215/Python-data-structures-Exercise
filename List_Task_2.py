"""Remove duplicates 
   Task: Use a loop or set() to eliminate repeated values. 
   Input: [1,2,2,3] 
   Output: [1,2,3]"""

def Dublicate_remover(your_list):
    set_list=set(your_list)
    My_list=list(set_list)
    print(f'Your list which you give"{your_list}\n After removing dublicates "{My_list}"')


a=[1,2,3,4,5,6,71,2,3,4,5,6,7]
Dublicate_remover(a)

