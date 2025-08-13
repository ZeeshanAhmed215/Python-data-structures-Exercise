"""Write list of strings to a file 
   Task: Write each string in a list as a separate line in a text file using writelines(). 
   Input: ["apple", "banana"]  
   Output: File with content: apple\nbanana """
fruit_list=['Apple','Orange','Banana','Mango']
with open("Fruits_file.txt","w") as file:
    for fruit in fruit_list:
        file.write(f'{fruit}\n')
with open("Fruits_file.txt","r") as file:
    for fruit in fruit_list:
        data=file.read()
        print(data)




