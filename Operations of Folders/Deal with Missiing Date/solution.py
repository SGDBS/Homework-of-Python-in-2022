s = input()
out = []
with open (r'./filldata.csv') as file:
    for line in file:
        initString = line.strip().split(',')
        for index, value in enumerate(initString):
            if value == '':
                initString[index] = s
        out.append(initString)
print(out)
