# # Imagine you're tracking the progress of a student in math and science across 10 tests. The provided code beautifully overlays the student's scores on the same chart using Matplotlib, enabling a visual comparison of the performances. Let's see how they've done!

# # Click Run to view the plotted scores!

import matplotlib.pyplot as plt
import numpy as np

# Data for student performance in two different subjects
math_scores = [88, 92, 80, 89, 85, 80, 60, 70, 60, 72]
science_scores = [72, 80, 78, 86, 94, 84, 76, 68, 72, 88]
tests = range(1, 11)  # Mock test numbers

# Plotting both subjects on the same axis
plt.ylim(0, 100)
plt.plot(tests, math_scores, label='Math scores', color='green', marker='o')
plt.plot(tests, science_scores, label='Science scores', color='blue', marker='x')
plt.title('Student\'s Tests Scores')
plt.xlabel('Test Number')
plt.ylabel('Score')
plt.legend()
plt.show()

# Splendid journey, Space Voyager! It's time to illuminate your code by filling in the stars.

# Make sure to overlay the academic trajectories of two students by adding both sets of data to the same plot. Use different colors to distinguish their individual journeys and add a legend for clarity. Good luck!

semesters = np.array([1, 2, 3, 4, 5, 6])
grades_student_A = np.array([3.2, 3.5, 3.7, 3.9, 4.0, 4.2])
grades_student_B = np.array([3.0, 3.3, 3.6, 3.8, 4.1, 4.3])

# TODO: Draw the line plot for Student A's grades using the blue color
plt.plot(semesters, grades_student_A, label='Student A', color='blue')  # Overlay Version A.
# TODO: Draw the line plot for Student B's grades using the green color
plt.plot(semesters, grades_student_B, label='Student B', color='green')  # Overlay Version A.

plt.title('Student\'s Tests Scores') # Adding title to our plot
plt.xlabel('Semester')
plt.ylabel('Mean Grade')
plt.legend()
plt.show()

# Plot your course, Space Explorer! Let's bring together the skills you've learned to track academic performance. Write code to plot a comparison for English and Math grades over several semesters. Ensure to overlay both data sets on the same plot.

# Remember to add legend, labels and title!

grades_english = np.array([80, 85, 88, 85, 90, 95, 97, 98])
grades_math = np.array([70, 75, 80, 78, 85, 90, 92, 94])
semesters = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# TODO: Add a plot for English grades
plt.plot(semesters, grades_english, label='English Student\'s', color= 'red')

# TODO: Add a plot for Math grades
plt.plot(semesters, grades_math, label='Math Student\'s', color='gray')

# TODO: Show the plots with legend, labels and title.
plt.title('Student\'s Tests Scores')
plt.xlabel('Semesters')
plt.ylabel('Mean Grade')
plt.legend()
plt.show()

# Would you like to track the progression of two students' academic achievements throughout their high school years? The given code compares the grades of two students over a three-year period using subplots. Click Run to view the side-by-side bar charts and discover how each student performed each year!

fig = plt.figure()

# Data for two students' grades over three academic years
grades_student_A = np.array([3.5, 3.7, 4.0])
grades_student_B = np.array([3.8, 3.9, 4.1])
years = np.array([1, 2, 3])

# Plot grades for student A in the first subplot
plt.subplot(1, 2, 1)
plt.bar(years, grades_student_A, color='blue', label='Student A')
plt.ylabel('Mean Grade')
plt.xlabel('Year')
plt.title("Student A")
plt.legend()

# Plot grades for student B in the second subplot
plt.subplot(1, 2, 2)
plt.bar(years, grades_student_B, color='green', label='Student B')
plt.ylabel('Mean Grade')
plt.xlabel('Year')
plt.title("Student B")
plt.legend()

plt.subplots_adjust(wspace=0.5)
fig.suptitle('Performance Comparison')

plt.show()

# Great job so far! Now let's apply what you've learned about subplots. Can you set up a bar plot for Student B on the right side of our figure? Remember to give it a title, labels and a legend. Also, provide the whole figure with a suptitle

# Performance of Student A and B in three different subjects
subjects = ['Math', 'Science', 'History']
student_a_grades = [85, 90, 75]
student_b_grades = [78, 88, 85]

fig = plt.figure()

# Creating a figure with 1 row and 2 columns for side-by-side comparison
plt.subplot(1, 2, 1)
plt.bar(subjects, student_a_grades, color='blue', label='Student A')
plt.xlabel('Year')
plt.ylabel('Mean Grade')
plt.title('Student A Grades')
plt.legend()

# TODO: Create a bar plot for Student B in the second subplot area.
# Add a title and labels to the subplot and a legend to identify Student B.
plt.subplot(1, 2, 2)
plt.bar(subjects, student_b_grades, color='brown', label='Student B')
plt.xlabel('Year')
plt.ylabel('Mean Grade')
plt.title('Student B Grades')
plt.legend()

# TODO: add a suptitle to the figure.
plt.subplots_adjust(wspace=0.5)
fig.suptitle('Performance Comparison')

plt.show()