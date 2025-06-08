data =open("data.dat").read()
rowfinder = data.split("\n")
rows = len(rowfinder)-1 #remove the last new line
columns = len(rowfinder[0].split())
print("number of rows is ",rows," numbers of columns is ",columns)
