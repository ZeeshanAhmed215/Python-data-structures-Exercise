"""2.Check if a string is a palindrome 
    Task: A palindrome reads the same forwards and backwards. Write a function to check 
    this. 
    Input: "radar" 
    Output: True """


def Checking_palindrome(String):
    your_string=String.lower()
    if your_string[0]==your_string[-1]:
        print(f' Yes!"{String}" is a palindrom. ')
    else:
        print(f' No!"{String}" is not a palindrom. ')


Checking_palindrome("Radar")