price = 50

inserted_total = 0

while inserted_total < price:
    inserted = input('Insert a coin: ')
    match inserted:
        case '50':
            inserted_total += 50
            #print('0')
            break
        case '25':
            inserted_total += 25
        case '10':
            inserted_total += 10
        case '5':
            inserted_total += 5
    if price-inserted_total > 0:
        print(f'Amount due: {price-inserted_total}')
owned = inserted_total - price

print('Change owed',owned)