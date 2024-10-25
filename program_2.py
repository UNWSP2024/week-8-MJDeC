# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13
sentence=input('Enter a sentence with no spaces, but capitalize the beginning of each word.')
def word_separator(sentence):

    new_sentence = ''
    #    Add your logic here
    #sentence=input('Enter a sentence with no spaces, but capitalize the beginning of each word.')
    final = ''
    for i in range(1,len(sentence)):
        char = sentence[i]
        if char.isupper():
            char = char.lower()
            final = final + ' '
        final = final + char
    return final.strip()

# Example usage

#sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(sentence[0]+new_sentence+'.')
