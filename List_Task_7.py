
"""Rotate list by k elements 
   Task: Use slicing to rotate a list left or right. 
   Input: [1,2,3,4], k=2 
   Output: [3,4,1,2] """


def rotate_list(num_list, Rotate_number):
    Rotate_number = Rotate_number % len(num_list)  
    Rotated_list = num_list[-Rotate_number:] + num_list[:-Rotate_number] 
    print(f'Your Rotated List is "{Rotated_list}"') 

List_of_numbers = [1, 2, 3, 4, 5]
print(f'Your given list"{List_of_numbers}"')
int=int(input("Enter a rotate number:}"))
if int>len(List_of_numbers):
    print(f'You entered a number "{int}" and the length of list is "{len(List_of_numbers)}"\n {int} > {len(List_of_numbers)}')
else:
    rotate_list(List_of_numbers,int)