import random


"""

2019_07_24
By Andy Clymer for Type@Cooper students


This is a MetricsMachine Words List script that we put together as a class.

Consider this to only be a starting point! Be sure to proof your figures, punctuation, symbols, etc...
However, those might not need to be formatted into words. The "Pair List Builder" in MetricsMachine should do fine.

It can also be sped up and optimized in a lot of ways, but it's still pretty useful as it is!

Change the settings in two places:
    1) Make sure that the wordFilePath points to a text file of proofing words
            I'm including a "Mini" list for testing while you edit the code,
            and a "Full" version that takes longer to run but has many many more words
    2) At the bottom of this script, tell the buildProof function which lists of letters to use
            buildProof(lowerLeft, lowerRight)
            
"""



# A path to a dictionary file full of words
# Edit this path so that it points to an actual text file that has a list lf words
wordFilePath = "ScrabbleWordList-Full.txt"

# Open the file, and read out the text
wordFile = open(wordFilePath, "r", encoding="utf-8")
wordText = wordFile.read()
# Split the text at each new line "\n" so that each word is on its own
wordList = wordText.split("\n")



def findWord(leftLetter, rightLetter):
    # A function to find a word fron the wordList that has this pair of letters
    
    # Make a comparison to figure out of the letter is upper or lower case
    leftIsUpper = leftLetter.upper() == leftLetter
    rightIsUpper = rightLetter.upper() == rightLetter
    
    # An empty list to collect all of the matching words in
    matchingWords = []
    
    # One at a time, look at each of the words in the wordList
    for word in wordList:
        
        # Based on the capitalization of the letters in the pair,
        # should this find a word with the pair in the middle of the word
        # or should it find one with the pair at the start of the word?
        findMidPair = True
        if leftIsUpper == rightIsUpper == True:
            word = word.upper()
        elif leftIsUpper == rightIsUpper == False:
            word = word.lower()
        else:
            word = word.title()
            findMidPair = False
        
        # If it should find one at the middle of the word
        if findMidPair:
            # Check to see if these two letters are in the range of letters
            # not counting the first and last letter
            if leftLetter + rightLetter in word[1:-1]:
                # If it finds one, add it to the matchingWords list
                matchingWords.append(word)
        else:
            # Otherwise, check to see if this pair is at the start of the word
            if leftLetter + rightLetter == word[0:2]:
                # If it finds one, add it to the matchingWords list
                matchingWords.append(word)
    
    # It's finished looking at every single word, to see if this pair is in the word
    # If it found more than zero matching words:
    if len(matchingWords) > 0:
        # Choose a random one from the list
        chosenWord = random.choice(matchingWords)
    else:
        # It couldn't find a word, make one up with the makeWord function
        chosenWord = makeWord(leftLetter, rightLetter, leftIsUpper, rightIsUpper)

    # All done, return the chosenWord back to whatever called the findWord() function
    return chosenWord



def makeWord(leftLetter, rightLetter, leftIsUpper, rightIsUpper):
    # This function will make up a new word for this pair of letters
    # The letters will be between neutral control characters "HO" or "no"
    
    # Start an empty new word
    newWord = ""
    
    if leftIsUpper and not rightIsUpper:
        # If the left is upper and the right is lower, make a word with this pair at the start
        newWord = leftLetter + rightLetter + "noners"
    else:
        # Format controls before the left letter
        if leftIsUpper:
            newWord += "HOH" + leftLetter
        else:
            newWord += "non" + leftLetter
        # Format controls after the right
        if rightIsUpper:
            newWord += rightLetter + "HOH"
        else:
            newWord += rightLetter + "non"
        
    # It's finished, return the word to whatever called the makeWord() function
    return newWord
    


def buildWordList(leftLetters, rightLetters):
    # Process through the pair lists.
    # For every combination of left and right letters...
    for leftLetter in leftLetters:
        for rightLetter in rightLetters:
            # Find a word
            word = findWord(leftLetter, rightLetter)
            # MetricsMachine needs a space between the letters of the pair
            # Replace the pair with a version of the pair that has a space in the middle
            # The 1 at the end of replace means that it should only replace the first instance of the pair
            pair = leftLetter + rightLetter
            pairWithSpace = leftLetter + " " + rightLetter
            word = word.replace(pair, pairWithSpace, 1)
            # ...and print the word
            print(word)
        



# The alphabet reordered so that similar letters are next to each other
# For instance, when the "H" is the left letter in the pair, you might want 
# the left letter in the next word to be "I" becaus they're similar in shape
capsLeft = "HIMNUJODQGPRSCEFLTZYAVWXK"
capsRight = "HIMBDNEKFLPRUOQCGAVWXYZTJS"
lowerLeft = "nmhuldqijgaobpestfrckxzvwy"
lowerRight = "nmplbhkirutfaocedqgjsvwyxz"

punctuation = ",.:-"

# A word list needs to start with a line that has the proof name
proofName = "UC - UC"
print("#KPL:W: " + proofName)

# Run the buildProof function here, to build the proof
# Tell it the name of the alphabet list for the left and right side of the pair
buildWordList(capsLeft, capsRight)

