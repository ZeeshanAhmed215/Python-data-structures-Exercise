"""Read a file line by line 
   Task: Use open() to read a file and loop through each line using a for loop. 
   Input: sample.txt 
   Output: Line 1\nLine 2 """

with open("Fruits_file.txt","r") as file:
   data=file.read()
   print(data)
   

