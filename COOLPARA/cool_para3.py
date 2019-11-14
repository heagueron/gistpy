# custom exception and try/exception block

import sys


text = sys.argv[1]

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class LineTooShortError(Error):
   """Raised when the input value is too small"""
   def __init__(self):
       print("The input line must contain at least 3 words")
   pass

def butlast(text):
    words = text.split()
    reduced_words = words[:-1]
    return ' '.join(reduced_words)

def CoolPara(text):

    #assert (len(text.split()) >= 3), "Input line must contain at least 3 words."
    
    words = text.split()
    counter_rare = 0
    counter_8 = 0

    for word in words:        
        if('j' in word or 'x' in word or 'q' in word or 'z' in word):
            counter_rare += 1
        if len(word) >= 8:
            counter_8 += 1

    print (f"Number of words: {len(words)}" )
    print (f"Number of words with rare letter: {counter_rare}")
    print (f"Number of words 8 letters or longer: {counter_8}" )

    print("*****")

    if ( len(words) > 10 and (counter_rare/len(words)) >= 0.1 and (counter_8/len(words)) >= 0.1 ):
        return True
    return False


try:
    if (len(text.split()) < 3):
        raise LineTooShortError
except LineTooShortError as error:
    print(error)
    print( "Counting was not executed.")
else:
    print(CoolPara(text))
    print(butlast(text))

print("Executed after the try/except block.")