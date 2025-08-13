""" Remove duplicate characters from a string 
   Task: Create a new string by keeping only the first occurrence of each character. 
   Input: "programming" 
   Output: "progamin" """
def Dublicate_remover():
    String=input("Enter your String:}")  
    
    string_set=set()
    string_list=[]
    for char in String:
        if char not in string_set:
            string_list.append(char)
            string_set.add(char)

    for char in string_list:
        print(char,end="")
        
    # return ''.join(string_list)

Dublicate_remover()





