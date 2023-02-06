dict = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

Total = 0.0
while True:

    try:
        user_input = input('Item: ').casefold()
        Total += dict[user_input]
        print(f'Total: ${Total:.2f}')
    except EOFError:
        break
    except KeyError:
        pass




print('\n')