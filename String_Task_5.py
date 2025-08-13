"""Replace substring without using .replace() 
   Task: Create a function that takes a main string, a target substring, and a replacement 
   substring and replaces the target manually. 
   Input: ("hello world", "world", "Python") 
   Output: "hello Python"""

def Replace(Full_String ,Sub_String, Replace_String):
    Words= Full_String.split(" ")
    print(Full_String)
    index=Words.index(Sub_String)
    Words.remove(Sub_String)
    Words.insert(index,Replace_String)

    for i in Words:
        print(i,end=" ")
        
Replace("How are you dua","dua","tayyaba")





