# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def main():
  cont='y'
  course_ids={}
  while cont=='y':
    course_input1=input("Enter a subject ID.")
    course_input2=input("Enter the subject name.")
    course_ids[course_input1]=course_input2
    cont=input("Enter y to add more course values. Enter another letter key to continue.")
  else:
    print(course_ids)
    choose=input("Enter a subject to see the IDs and names for that subject.")
    for course_input1,course_input2 in course_ids.items():
      if choose in course_input1:
        print(course_input1,course_input2)
      else:
        print('ID not found.')
  
main()
