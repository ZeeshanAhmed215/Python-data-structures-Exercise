"""Save dictionary as JSON and load 
   Task: Use json.dump() to write dictionary to a file and json.load() to read it. 
   Output: {'name': 'John'} saved/loaded """
import json
Students={'Abdul Ahad':90,'Dua Ali':87,'Muddasir':89}
with open("Students_marks.json",'w') as file:
    json.dump(Students,file)


with open("Students_marks.json",'r') as file:
    data=json.load(file)
    print(data)