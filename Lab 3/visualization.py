import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D', 'E']
marks = [75, 82, 91, 68, 88]

plt.bar(students, marks)
plt.title('Student Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

plt.plot(students, marks, marker='o')
plt.title('Marks Trend')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()
