"""Copy contents from one file to another 
Task: Open the source file in read mode and destination in write mode to copy contents. 
Output: Duplicate file created """
with open("Fruits_file.txt","r") as file:
        data_1=file.read()
with open("Fruits_file2.txt","w") as file:
        file.write(data_1)

