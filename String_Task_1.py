"""1.Reverse a string 
   Task: Write a function that takes a string as input and returns the reversed string using 
   slicing or a loop. 
   Input: "hello" 
   Output: "olleh" """



def String_Reverser(String):
    last_char=String[-1:]
    sum=""
    for i in range(len(String)):
        i=i+1
        i=-i
        Char= String[i:i+1]
        sum+=Char
        
    print(f'Your given string "{String}" and reversed string "{last_char+sum}"')


String_Reverser("noonari")



















    





# print(a[-1:])
# print(a[-2:-1])
# print(a[-3:-2])
# print(a[-4:-3])
# print(a[-5:-4])

