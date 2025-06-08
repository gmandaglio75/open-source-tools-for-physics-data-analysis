data1 =open("data.dat").read().split("\n")
data2 = [list(map(float,data1[i].split())) for i in range(len(data1)-1)]
data = []
for a in range(len(data2)):
    data.append(data2[a][1])
print(data)
data.sort()
print(data[0])
print(data[len(data)-1])
