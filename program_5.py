# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def main():
  cont='y'
  course_ids={}
  if cont=='y':
    cont=input("Enter y to add more course values. Enter another letter key to continue.")
    course_input1=input("Enter a subject letter tag:")
    course_input2=input("Enter a course ID number to go with the letters:")
    course_input3=input("Enter the corresponding course name:")
    course_ids={course_input1,course_input2,course_input3}
    cont=input("Enter y to add more course values. Enter another letter key to continue.")
  else:
    choose=input("Enter a subject to see the IDs and names for that subject.")
    course_list=course_ids.get(choose,'No courses with that ID are entered.')
    print(course_list)
  
main()
