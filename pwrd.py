import sys
# Import the random library that supports the random function
import random

# This is a list of several symbols
symlist = ['!','@','#','$','%','^','&','*','(',')','?','-','=','_','+','<','>',',','.','/',';',':','"','[',']','{','}','|']

# Open the file that has the diceware dictionary
response = open('/Users/tenboj/Desktop/diceware.wordlist.asc', 'r')

# Create a list from a local diceware dictionary file
mywords = {}
for line in response:
        listindex, word = line.strip().split('\t')
        mywords[int(listindex)] = word

# The password is several words, so create a empty passphrase list
passphrase = []
intwords = 5

# Step 1) Simulate 5 dice rolls and concatenate those 5 digits.
# Step 2) Once concatenated, lookup diceware dictionary for a word match
# Then, repeat steps above x times for x words
for y in range(0, intwords):
        pw=str();

        # Create 5 digit index for diceware dictionary
        for x in range(0, 5): pw+=str(random.SystemRandom().randint(1, 6))

        # Retrieve word from diceware dictionary
        word = mywords[int(pw)]

        # Randomly capitalize the word
        if random.SystemRandom().randint(0, 1) == 1:
                word = str.capitalize(word)

        # Append word to the passphrase
        passphrase.append(word)

# Convert passphrase to string and append a random symbol from symlist
strpassphrase = ' '.join(passphrase) + symlist[random.SystemRandom().randint(0, len(symlist)-1)]

# Print out passphrase
print '\n' + strpassphrase + '\n'
