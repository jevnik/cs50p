a = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input('Date: ').strip()
    try:
        month,day,year = user_input.split('/')
        month = int(month)
        day = int(day)
        if day < 32  and month < 13:
            if day < 10:
                day = f'0{day}'
            if month < 10:
                month = f'0{month}'
            print(f'{year}-{month}-{day}')

            break
    except:
        pass
    try:
        month,day,year = user_input.split()
        month_num = a.index(month) +1
        month_num = int(month_num)
        day = day[:-1]
        day = int(day)
        if day < 32 and month_num < 13:
            if day < 10:
                day = f'0{day}'
            if month_num < 10:
                month_num = f'0{month_num}'
            print(f'{year}-{month_num}-{day}')
            break
    except:
        pass