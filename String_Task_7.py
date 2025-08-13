""" Count frequency of each character 
    Task: Use a dictionary to count how many times each character appears in the input 
    string. 
    Input: "hello" 
    Output: {'h':1, 'e':1, 'l':2, 'o':1}"""
def frequency_counter():
    input_string=input("Enter your string:}")
    Dic={}

    for x in input_string:
        coun=input_string.count(x)
        Dic[x]=coun
    print(Dic)
 

frequency_counter()