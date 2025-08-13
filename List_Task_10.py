"""Generate power set of list 
   Task: Use itertools combinations() to generate all subsets. 
   Input: [1,2] 
   Output: [[], [1], [2], [1,2]] """
Given_list=[3,2,1]

def Lowest(Num_list):
    x=None
    for i in Num_list:
        if x is None:
            x=i
        elif i<x:
            x=i
    return x



def Assending(Num_list):
    Assending_list=[]
    for i in range(len(Num_list)):
        lower_num=Lowest(Num_list)
        Assending_list.append(lower_num)
        Num_list.remove(lower_num)
    return Assending_list

Assending_order_list=Assending(Given_list)
Double=[]
Single=[[]]

for i in Assending_order_list:
    c=[i]
    Single.append(c)

for i in range(len(Assending_order_list)-1):
    # print(i+2)
    b= Assending_order_list[0:i+2]
    Double.append(b)

print(f'Actual list:"{Assending_order_list}"')
print(f'Subset:"{Single+Double}"')