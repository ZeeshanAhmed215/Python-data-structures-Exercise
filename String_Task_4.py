"""4.Convert to title case without using .title() 
   Task: Capitalize the first letter of each word manually using string methods like 
   .split() and .capitalize(). 
   Input: "hello world" 
   Output: "Hello World"""


def Converting_Tittle(S):
    Words=S.split()
    Title_case_words=[]
    for word in Words:
        Title_case_words.append(word.capitalize())

    print(" ".join(Title_case_words))


Converting_Tittle("how are you ")
