"""dictionary = {"bug": "an error of a program that prevents the program from running as expected. ",
              "Function": "A piece of code that you can easily call over and over."}
print(dictionary["Function"])

dictionary["loop"] = "The action of doing something over and over again."
#print(dictionary)
#wipe an existing dictionary
#empty_dictionary = {}
#dictionary = {}
#print(dictionary)

#edit an item
dictionary["bug"] = "A moth in your computer"
print(dictionary)
#loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])"""
"""Grading Program exercise
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores. 
Write a program that converts their scores to grades.
By the end of your program, you should have a new dictionary called student_grades 
that should contain student names as keys and their assessed grades for values. 
The final version of the student_grades dictionary will be checked. """

student_scores = {"rosy":71,
                  "liza":93,
                  "lipan": 89,
                  "shen": 60}
student_grades = {}
for key in student_scores:
    if (student_scores[key] > 90 and
            student_scores[key] <= 100):
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80 and student_scores[key] <= 90 :
        student_grades[key] = "Exceeds expectations"
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)












