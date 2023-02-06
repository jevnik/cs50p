grocery = {}
while True:

    try:
        a = input("").casefold()
        grocery[a] += 1
    except EOFError:
        break
    except KeyError:
        grocery[a] = 1
print()

keys = []
for item in grocery:
    keys.append(item)

keys.sort()

sorted_grocery = {}

for key in keys:
    sorted_grocery[key] = grocery[key]

for item in sorted_grocery:
    print(grocery[item], item.upper())
