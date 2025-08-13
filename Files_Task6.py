"""Create a log writer with timestamps 
Task: Append a log entry to a file, each entry should contain a datetime stamp. 
Output: [2025-07-13 10:00] Event logged """
import datetime
Tim=datetime.datetime.now()
Time=Tim.strftime(f"%d-%m-%Y %H:%M:%S")
Time_logo=f'[{Time}]'
with open("Fruits_file2.txt","a") as file:
        file.write(f'\n{Time_logo}\n Write here!.............')
