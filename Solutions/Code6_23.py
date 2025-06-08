#by coluns
even = [a for a in range(0,100,2)]
odd  = [a+1 for a in range(0,100,2)]
sum  = [even[a]+odd[a] for a in range(50)]
solution = [even,odd,sum]
print("by columns**********")
print(solution)
#by rows
print("by rows**********")
solution = [[even[a],odd[a],sum[a]] for a in range(50)]
print(solution)
#in C++-Style
print("by rows in c++Style**********")
rows, cols = (50, 3)
solution = [[0 for i in range(cols)] for j in range(rows)]
for i in range(50):
    solution[i][0] = 2*i
    solution[i][1] = solution[i][0] +1
    solution[i][2] = solution[i][0] + solution[i][1]
print(solution)
