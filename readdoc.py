file = open("C:\\Users\\User\\Desktop\\data.txt")

line_list = file.readlines()

for line in line_list:
    z = line.split()
    for i in z:
        if i == "9,314" or i == "Q4-2020":
            print(line)

zap=","
s=""


z = line.split()
for i in z:
    for j in i:
        if(j.isdigit()):
          s+=i+" "
          break
print(z)
z=""
for i in range(len(z)):
    if(s[i]!=","):
        z+=s[i]
    elif(s[i]==","):
        z+="."
z=z.split()
print(z)



file.close