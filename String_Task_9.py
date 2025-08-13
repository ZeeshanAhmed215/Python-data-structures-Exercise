"""Check if two strings are anagrams 
   Task: An anagram contains the same characters in different order. Sort both and 
   compare. 
   Input: ("listen", "silent") 
   Output: True 
"""

def Anagrams():
    Word_first=input("Enter first word:}")
    Word_second=input("Enter second word:}")
    First_word_list=[]
    Second_word_list=[]
    for x in Word_first:
        First_word_list.append(x)
    for x in Word_second:
        Second_word_list.append(x)   


    sort_one=sorted(First_word_list)
    sort_two=sorted(Second_word_list)
    if sort_one==sort_two:
        print(f' Yes "{Word_first.capitalize()}" and "{Word_second.capitalize()}" are anagrams!')
    else:
        print(f' No! "{Word_first.capitalize()}" and "{Word_second.capitalize()}" are not anagrams!')

Anagrams()