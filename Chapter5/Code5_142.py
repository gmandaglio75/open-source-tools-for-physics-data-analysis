import matplotlib.pyplot as plt

# Data
classes = ['Class A', 'Class B', 'Class C', 'Class D']
students = [23, 17, 35, 29]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(classes, students, color='skyblue')
plt.xlabel('Classes')
plt.ylabel('Number of Students')
plt.title('Number of Students in Different Classes')
plt.show()
