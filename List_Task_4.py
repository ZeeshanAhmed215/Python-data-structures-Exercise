""" Find second largest number 
Task: Remove max and find new max from remaining list. 
Input: [4,1,3,2] 
Output: 3 """
def Highest(Num_list):
    x=-1
    for i in Num_list:
        if i >x:
            x=i
    return x

def Second_largest(Num_list):


    Num_list.remove(Highest(Num_list))
    s=Highest(Num_list)
    print(s)

Second_largest([4,1,3,2])