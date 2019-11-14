# assert inside main function and try/exception block

import sys


text = sys.argv[1]

def CoolPara(text):

    assert (len(text.split()) >= 3), "Input line must contain at least 3 words."
    
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

# try:
#     print( CoolPara(text) )
# except:
#     print( "Counting was not executed")

# print("Executed after the try/except block")

try:
    print( CoolPara(text) )
except AssertionError as error:
    print(error)
    print( "Counting was not executed.")
else:
    print("Executing the else clause.")

print("Executed after the try/except block.")