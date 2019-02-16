# Assignment 7 - Question 1
# Submitted By:  Ritvik Khanna   &    Bisan Hasasneh
#                   1479093      &       1505703 

import math,sys,random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():


    # For testing purposes only

    key = 'WICK'
    text = 'THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY'

    finalCipher = antiKasiski(key,text)

    print(finalCipher)


def antiKasiski(key,plaintext):

    newPlainText = '' 

    # ***** Step1: Getting rid of non-letters ***** #

    for symbol in plaintext:

        if symbol.upper() in LETTERS:

            newPlainText += symbol


    # ***** Step2: obtaining ciphertext from vigenereCipher using encryptMessage(key,message) and translateMessage(key,message,mode) ***** #

    translated = encryptMessage(key,newPlainText)

    plaintext = newPlainText

    # ***** Step3: Loop until there are no repeated sequence in the ciphertext of atleast length 3 ***** #
    # For this part changes were made to the findRepeatSequencesSpacings fucntion - See comments in that function

    while(findRepeatSequencesSpacings(translated) != None):

        plaintextList = list(plaintext)

        position = findRepeatSequencesSpacings(translated)

        plaintextList.insert(position, random.choice(LETTERS))

        plaintext =  ''.join(plaintextList)

        translated = encryptMessage(key,plaintext)

    if(findRepeatSequencesSpacings(translated) == None):
        print("Kasiski Examination failed")


    # ***** Step4: Returning the final Ciphertext after the very last iteration through the loop ***** #

    return translated


   

# Copied as it is from vigenereCipher.py mentioned on inventwithpython.com/hacking
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


# Copied as it is from vigenereCipher.py mentioned on inventwithpython.com/hacking
def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)




# Copied from viegenereHacker.py published as a source code on inventwithpython.com/hacking
def findRepeatSequencesSpacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).

    # Compile a list of seqLen-letter sequences found in the message.
    seqSpacings = {} # keys are sequences, values are list of int spacings
    posList = []
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = message[seqStart:seqStart + seqLen]

            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # initialize blank list

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seqSpacings[seq].append(i - seqStart)


                    # ***** We made just a small change - returning just the position of the first character of the 2nd occurrence in the ciphertext
                    return i  
    return None # **** Coding such that if there are no sequences return None


if __name__ == '__main__':
            main()


                               
