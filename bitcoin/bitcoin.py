import sys
import requests

try:
    btcs = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
except IndexError:
    sys.exit('Missing command-line argument')


api_btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

btc_price = api_btc['bpi']['USD']['rate_float']

res = round(btcs * btc_price,4)

res = f'${res:,f}'

print(res[:-2], end='')

