""" Find all pairs with given sum 
    Task: Use two loops or set to find pairs with sum = target. 
    Input: [1,2,3,4], target=5 
    Output: [(1,4), (2,3)] """
Num_list=[1,2,3,4,5,6,7,8,9,10]
l=[]
for i in Num_list:
    for j in Num_list:
        if j+i==5:
            b=t=(i,j)
            l.append(b)
print(l)
