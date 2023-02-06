fruit = input('Fruit: ')
fruit = fruit.casefold()

dic = {
    'apple' : 130,
    'avocado' : 50,
    'banana' : 110,
    'cantaloupe' : 50,
    'grapefruit' : 60,
    'grapes' : 90,
    'Honeydew melon' : 50,
    'kiwifruit' : 90,
    'lemon' : 15,
    'lime' : 20,
    'nectarine' : 60,
    'orange' : 80,
    'peach' : 60,
    'pear' : 100,
    'pineapple' : 50,
    'plums' : 70,
    'strawberries' : 60,
    'sweet cherries' : 100,
    'tangarine' : 50,
    'watermelon' : 80
    }
if fruit in dic:

    print('Calories:',dic[fruit])