"""Merge two files line by line 
   Task: Read one line from each file and write combined lines to a new file. 
   Output: Merged output in new file """
def Merge_File(File1,File2):
   with open(File1,'r') as file:
      data1=file.read()

   with open(File2,'r') as file:
      data2=file.read()

   with open('Merge_file.txt','w') as file:
      file.write(f'{data1}\n{data2}')

      
Merge_File("File1.txt","File2.txt")