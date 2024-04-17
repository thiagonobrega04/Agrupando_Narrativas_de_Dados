# Lesson Overview: Crafting Your Data Storybook
# Welcome to our storytelling session, where data comes alive on the pages of Matplotlib! Today, you'll become adept at weaving multiple data narratives together on a single canvas. This process is much like assembling a scrapbook, where every photo, or in this case, plot, adds depth to the story. By the end of this lesson, you'll know how to create a multi-plot narrative using layers on the same axis and within a single figure.

# Understanding Subplots and Axes
# Imagine you're building a scrapbook. Each page can hold multiple pictures, and you can decide where each photo goes. Subplots work similarly, helping us position multiple charts within a plot grid. We'll learn how to organize our data tales neatly on a page using subplots.

# Here's a detailed example of creating subplots:

import matplotlib.pyplot as plt
import numpy as np

plt.figure()  # Start a new figure, your scrapbook page.

x1 = np.array([0, 1, 2])
y1 = np.array([0, 1, 4])
# Begin a subplot grid: 1 row and 2 columns.
plt.subplot(1, 2, 1)  # First plot area (row 1, col 1 of 2, position 1).
plt.plot(x1, y1)  # Plot a line representing our first story.
plt.title('Plot 1')  # Adding title to our first plot

x2 = np.array([0, 1, 2])
y2 = np.array([0, 2, 3])
plt.subplot(1, 2, 2)  # Second plot area (row 1, col 2 of 2, position 2).
plt.plot(x2, y2)  # Next to it, a related tale.
plt.title('Plot 2')  # Adding title to our first plot

plt.show()  # Like turning the scrapbook page to view all photos.

# Let's decipher plt.subplot(1, 2, 1): 1, 2 defines a grid of one row and two columns, and the last 1 specifies the first column for our plot. This ensures your plots are arranged like photos on a scrapbook page, telling parts of the bigger story side by side.

# Placing two plots near help us to gather data visualization in one place making it easier for the viewers to compare and connect pieces of information.

# Students Performance Dataset
# Let's consider a more meaningful dataset. Imagine we have this data for two students average marks and want to compare their performance with plots:

first_student_marks = np.array([3.8, 3.9, 3.8, 4.1, 4.4, 4.2, 4.5, 4.5, 4.7])
second_student_marks = np.array([4, 3.9, 4.1, 4.1, 4.1, 3.9, 3.8, 3.7, 3.5])
semesters = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Plotting Students Performance
# Here is how we will plot these graphs:

fig = plt.figure()  # Start a new figure

# Begin a subplot grid: 1 row and 2 columns.
plt.subplot(1, 2, 1)
plt.ylim([3, 5])
plt.xticks([0, 3, 6, 9])
plt.xlabel('Semester')
plt.ylabel('Mean Score')
plt.plot(semesters, first_student_marks)
plt.title('student A')

plt.subplot(1, 2, 2)
plt.ylim([3, 5])
plt.xticks([0, 3, 6, 9])
plt.xlabel('Semester')
plt.ylabel('Mean Score')
plt.plot(semesters, second_student_marks)
plt.title('student B')

plt.subplots_adjust(wspace=0.5)  # Adjusting horizontal space
fig.suptitle('students\' performance')  # Adding main title to the whole figure

plt.show()

# Notice a couple of things. Firstly, plt.ylim function ensures plots have equal y-axis limits, making the comparison more clear. Secondly, the figure is saved in the fig variable, which lets us add a main title using fig.suptitle function. Finally, we use the new plt.subplots_adjust function with a variable wspace parameter to ensure there is enough place between the subplots.

# Having two plots side-to-side plots lets us both investigate individual graphs and easily compare them to each other.

# Layering Plots on the Same Axis
# There is another way to compare these plots.

# To tell a rich story, we often combine multiple elements on the same page, like overlaying transparent leaves over a photo. Similarly, we can overlay plots on the same axis in Matplotlib, comparing different datasets directly.

# Combining two plots on one axis is easy: call the plt.plot function twice!

plt.plot(semesters, first_student_marks, label='Student 1', color='purple')  # Overlay Version A.
plt.plot(semesters, second_student_marks, label='Student 2', color='orange')  # Overlay Version B.
plt.title('Students\' Performances')  # Adding title to our plot
plt.xlabel('Semester')
plt.ylabel('Mean Score')

plt.legend()  # Clarify which line refers to each version.
plt.show()

# Notice that the plt.legend() function acts as a caption beneath our photo, helping readers understand which element is within the story's overlay.

