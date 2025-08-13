"""Merge two dictionaries 
   Task: Use unpacking or update() method. 
   Input: {'a':1}, {'b':2} 
   Output: {'a':1, 'b':2}"""
dic_1={"Zeeshan":77,"Ahad":90}
dic_2={"Dua":78,"Tayyaba":99}
dic_1.update(dic_2)
print(dic_1)