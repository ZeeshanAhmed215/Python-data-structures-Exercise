""" Sort words alphabetically in a sentence 
    Task: Split the sentence into words and sort them using the sorted() function. 
    Input: "python is great" 
    Output: ['great', 'is', 'python'] """


def Sentence_sorting():
    sentence=input("Enter your sentences:}")
    Split= sentence.split(" ")
    sorted_list=sorted(Split)
    for i in sorted_list:
        print(i,end=" ")


Sentence_sorting()