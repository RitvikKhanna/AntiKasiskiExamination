# Assignment 7 - Question 2,3,4 (Combined)
# Submitted By:  Ritvik Khanna      &       Bisan Hasasneh
#                  1479093          &          1505703 
# The line of the code 
# list1 = sorted(list1, key=lambda x: x[1],reverse = True) was taken from stackoverflow - https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value 

import math,sys,random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

    # For testing purposes only
   
    message = 'PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA'

    print(stringIC(message))

    print(keylengthIC(message))


# *** Question - 2 *** #

def stringIC(message):
    # Returns the index of coincidence for a string


    # Empty dictionary for getting the count for all the letters
    wordDict = {}

    sum1 = 0

    # Getting count of every character in the message
    for symbol in message:

        # getCount function returns the count of the particular letter in the message
        count = getCount(symbol,message)

        # Put that word with the count in the dictionary
        wordDict[symbol] = count


    # Finding the actual IC
    for key in wordDict:

        count = wordDict[key]

        # Numerator for the formula of IC 
        sum1 += count*(count-1)

    # Denominator for the formula of IC    
    N = len(message)*(len(message)-1)

    # Return the desired value
    return(sum1/N)




# ***  Question - 3 *** #
def subseqIC(ciphertext, keylen):
    # Calculates the average index of coincidence for all substrings
    # in a vigenere encrypted string given a keylength
    
    sumofICs = 0
    n = 0

    
    for i in range(keylen):
        
        # Get a substring (enciphered with a particular letter from the key)
        s = getNthSubkeysLetters(i, keylen,ciphertext)
        
        # increment count and record an IC for this substring
        n += 1
        sumofICs += stringIC(s)

    return(sumofICs/n)



# *** Question - 4 *** #
def keylengthIC(ciphertext):

    # Empty dictionary - with keys as key-lengths and value as their corresponding result of subseqIC
    keyList = {}

    # Empty list of top 5 possible keys
    possibleKeys = []

    # For all possible key-lengths 1 - 20 (including)
    for length in range(1,21):

        # Get the average
        average = subseqIC(ciphertext,length)

        # Entering the value in the dictionary
        keyList[length] = average

    # Make a list of the key and corresponding value in a tuple and append it to the list.
    # We converted it to the list to sort as we cannot sort the dictionary
    list1 = keyList.items()

    # The line below was taken from stackoverflow - https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # We did this to sort the list in descending order
    list1 = sorted(list1, key=lambda x: x[1],reverse = True)

    # Take the first 5 elements from the sorted list above and append it to the possibleKeys list.
    for i in range(0,5):

        possibleKeys.append(list1[i][0])

    # Return the list with the top 5 possible keys
    return(possibleKeys)
        

# *** This function was introduced for Question - 2 *** #
# This function returns the count of the particular symbol in the message passed.
# Example: For getCount(A,'ABA') - it returns 2
#              getCount(B,'ABA') - it returns 1
#              getCount(A,'AABCHJASGFA') - it returns 4
def getCount(symbol,message):

    count = 0

    for character in message:

        if(character == symbol):

            count += 1

    return(count)



# Taken from vigenereHacker.py published on - inventwithpython.com/hacking
def getNthSubkeysLetters(n, keyLength, message):
    # Returns every Nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)
        

    

if __name__ == '__main__':
            main()


                               
