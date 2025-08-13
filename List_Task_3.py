"""Sort list in ascending/descending order 
   Task: Use sorted() or .sort() with and without reverse flag. 
   Input: [3,1,2] 
   Output: [1,2,3] or [3,2,1] """



def Highest(Num_list):
    x=-1
    for i in Num_list:
        if i >x:
            x=i
    return x

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

def Desending(Num_list):
    Desending_list=[]
    for i in range(len(Num_list)):
        Highest_num=Highest(Num_list)
        Desending_list.append(Highest_num)
        Num_list.remove(Highest_num)
    return Desending_list


Numbers_list=[3,4,2,6,7,8,66,9,12,23,44]

Assending_num=Assending(Numbers_list)
Desending_num=Desending(Numbers_list)
print(f'Your given list:"{Numbers_list}"\nAssending:"{Assending_num}"\nDesending:"{Desending_num}"')












# num1_list=Num_list
# num2_list=[]
# # sort=sorted(Num_list)
# for i in range(len(Num_list)):
#     m=max(Num_list)
#     num2_list.append(m)
#     Num_list.remove(m)



# sorted_desending_list=num2_list
# print(f' Your list:"{Num_list}"\nAssending order:"{num2_list.sort()}"\nDesending order:"{sorted_desending_list}"')
