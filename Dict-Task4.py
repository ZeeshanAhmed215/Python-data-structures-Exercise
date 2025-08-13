"""Word frequency in a string 
   Task: Use a loop to count occurrences of each word. 
   Input: "hi hi hello" 
   Output: {'hi':2, 'hello':1} """
input_string=input("Enter your string::} ")
Split_string=input_string.split(" ")

ind=[]
dic={}
for x in Split_string:
    if x==x:
      co=Split_string.count(x)
      ind.append(co)

for x,y in zip(Split_string,ind):
   dic[x]=y

print(dic)