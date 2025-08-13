"""Append data to a file 
   Task: Use append mode ('a') to add new data to the end of an existing file. 
   Output: New line added """
with open("Fruits_file.txt","a") as file:
    file.write("Cherry\n")

