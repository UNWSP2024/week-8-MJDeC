# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13
def word_separator(sentence):

    new_sentence = ''
    #    Add your logic here
    sentence=input('Enter a sentence with no spaces, but capitalize the beginning of each word.')
    final = ''
    final = final+new_sentence[0]
    for i in range(1,len(sentence)):
        char = sentence[i]
        if char.isupper():
            char = char.lower()
            final = final + ' '
        final = final + char
        

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
