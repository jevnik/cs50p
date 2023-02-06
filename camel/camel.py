name = input('Name of a variable in camelCase: ')
res = ''
for i in range(len(name)):
    if name[i].isupper():
        res += '_'
        res += name[i].casefold()
    else:
        res += name[i]
print(res)