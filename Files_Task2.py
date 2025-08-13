"""Count lines, words, characters 
   Task: Count and return the total lines, word count, and number of characters in a file. 
   Output: 5 lines, 50 words, 300 characters """

def File_data_counter(File_path):
   lines=[]
   Words=[]
   Characters=[]
   with open(File_path,"r") as file: 
      data=file.read()
   #    print(data)
   # Counting Lines
      data_str=str(data)
      Split_data_line=data_str.split("\n")
      for x in Split_data_line:
         lines.append(x)
   # Counting Words
      for  line in lines:
         st=str(line)
         word_split=st.split(" ")
         for word in word_split:
            Words.append(word)

      for char in Words:
         for ch in char:
            Characters.append(ch)


   print(f'Lines: {len(lines)}')
   print(f'Words: {len(Words)}')
   print(f'Characters: {len(Characters)}')
      
      

File_data_counter("mple.txt")