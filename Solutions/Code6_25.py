import math
data = list(map(float,open("data.dat").read().split()))
mean = sum(data)/len(data)
gaps = [(data[i]-mean)**2. for i in range(len(data))]
rms = math.sqrt(sum(gaps)/len(gaps))
print("the mean value is ",mean,"  the standard deviation ",rms)
