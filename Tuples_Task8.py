""" Sort list of tuples by second element 
    Task: Use sorted() with key lambda. 
    Input: [(1,2),(3,1)] 
    Output: [(3,1),(1,2)] """
tup=[(1,2),(3,1)]
sorted_tuple=sorted(tup,key=lambda x: x[1])
print(sorted_tuple)


