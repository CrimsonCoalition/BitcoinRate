# Imports / Импорты
import requests
import sys
import locale
import rich
from rich.console import Console

console = Console()

## Banner & Menu / Баннер (лого) и менюшка
console.print("""
[italic blue]
    ____  _ __             _     
   / __ )(_) /__________  (_)___  by @CrimsonCoalition
  / __  / / __/ ___/ __ \/ / __ 
 / /_/ / / /_/ /__/ /_/ / / / / /
/_____/_/\__/\___/\____/_/_/ /_/ 

""")  


# Copyright Message / Копирайт
console.print("""                                                               
[italic red]
Copyright (C) 2022  CrimsonCoalition
Данный скрипт поможет вам узнать курс Bitcoin к Рублю.[/]
""", style = "magenta")

# Author's Channel Link
console.print("""
[bold green] :alien_monster: Канал автора: [link=https://t.me/crimsoncoalition]https://t.me/crimsoncoalition""")

# Menu
console.print("""[bold white]
На данный момент доступен курс BTC к RUB.

""")

TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

def get_latest_crypto_price(crypto):
  
  response = requests.get(TICKER_API_URL+crypto)
  response_json = response.json()
  
  return float(response_json[0]['price_usd'])

get_latest_crypto_price('bitcoin')

def main():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_latest_crypto_price(crypto)
  
    if price != last_price:
      console.print(''' [italic white] Цена Bitcoin: ''',price)
      last_price = price

main()      
