# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
def main():
  correct_score=0
  incorrect_score=0
  quiz_dictionary={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver','Conneticut':'Hartford',
                    'Delaware':'Dover','Florida':'Tallahassee'}
  for key,value in quiz_dictionary.items():
    guess=input('Guess the capital of this state:',key,'.')
    if guess==value:
      correct_score=correct_score+1
    else:
      incorrect_score=incorrect_score+1
    return main
print('Amount correct:',correct_score)
print('Amount incorrect:',incorrect_score)
main()                           
