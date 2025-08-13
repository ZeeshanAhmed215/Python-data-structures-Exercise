"""Remove empty lines from a file 
   Task: Read the file, filter out empty lines, and overwrite the file. 
   Output: File without blank lines"""
def Blank_line_remover(file_path):
    with open(file_path,'r') as file:
        data=file.read()
        data_list=data.split("\n")
    element_list=[]
    pure_elements=[]
    for index,element in enumerate(data_list):
        if element=="":
            pass
        else:
        
            element_list.append(index)
    for x ,y in zip(element_list,data_list):
        ele=data_list[x]  
        pure_elements.append(ele) 
    with open(file_path,'w') as file:
        for x in pure_elements:
            file.write(x+"\n")
    print(f'Check file {file_path}\nBlank lines have removed! ')
    
 
Blank_line_remover("Fruits_file.txt")

  
          

         

              
            










   

   


        



        


 