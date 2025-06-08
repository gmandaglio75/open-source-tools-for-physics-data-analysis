import matplotlib.pyplot as plt

# Data
classes = ['Class A', 'Class B', 'Class C', 'Class D']
students = [23, 17, 35, 29]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(students, labels=classes, autopct='%1.1f%%', startangle=140)
plt.title('Student Distribution')
plt.show()
