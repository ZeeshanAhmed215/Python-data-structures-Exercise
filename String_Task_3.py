"""3.Count vowels, consonants, digits, special characters 
     Task: Write a function to count and return the number of vowels, consonants, digits, and 
     special characters in a given string. 
     Input: "Hello123!" 
     Output: Vowels=2, Consonants=3, Digits=3, Special=1 """


def Count(String_U):
    String=String_U.lower()
    Vowels_list=[]
    Digits_list=[]
    Consonant_list=[]
    Special_list=[]
    Vowels="aeiou"
    Digits="0123456789"
    Consonant="bcdfghjklmnpqrstvwxyz"
    Special="!~`@$^&*()-\.,+=/><|"

    for V in Vowels:
        for S in String:
            
            if V==S:
                No=True
                Vowels_list.append(No)
    for D in Digits:
        for S in String:
            
            if D==S:
                No=True
                Digits_list.append(No)

    for C in Consonant:
        for S in String:
            
            if C==S:
                No=True
                Consonant_list.append(No)
    for Sp in Special:
        for S in String:
            
            if Sp==S:
                No=True
                Special_list.append(No)
    print(f'Your string: "{String_U}"\nVowels: {len(Vowels_list)}\nDigits: {len(Digits_list)}\nConsonant: {len(Consonant_list)}\nSpecial: {len(Special_list)}')


    

Count("noorcs29@gmail.com")


                   
                

            

 
        


