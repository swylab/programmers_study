str = input()
a = []
for i in range(len(str)):
    if str[i].isupper() == True:
        a.append(str[i].lower())
    else:
        a.append(str[i].upper())
a = "".join(a)
print(a)


