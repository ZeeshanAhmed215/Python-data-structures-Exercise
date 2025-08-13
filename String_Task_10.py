"""Caesar Cipher encoder (shift=3) 
   Task: Encode the input string using Caesar Cipher where each letter is shifted by 3 
   positions in the alphabet. 
   Input: "abc" 
   Output: "def" """

Alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string_input=input("Enter your alpha string::} ")
Index_list=[]
Char_list=[]


for i in string_input:
    for j in Alpha:
       if i==j:
           index=Alpha.index(i)
           Index_list.append(index)
        
for ind in Index_list:
    ch=Alpha[ind+3]
    Char_list.append(ch)

for char in Char_list:
    print(char,end="")



