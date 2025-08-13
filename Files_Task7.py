"""Read and format CSV file 
   Task: Read data from a CSV file and print in a formatted way using the csv module. 
   Input: data.csv 
   Output: Name: John, Age: 30 """

import csv
with open("Students.csv","r",newline="") as file:
    reader_file=csv.reader(file)
    
    for lines in reader_file:
        print(lines)
        