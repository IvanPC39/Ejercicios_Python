# Fechas

import datetime # Modulo para fechas 

now = datetime.datetime.now() #Recuerda llamar primero al modulo y despues a la función que quieras utilizar

print(now.day)

# Otra manera de hacerlo es:
from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.timestamp)

print_date(now)

new_year = datetime(2024, 1 , 1)

print(new_year)

from datetime import time

current_time = time(16, 39, 0) # Debes definirle los valores 

print_date(current_time.hour)
print_date(current_time.minute)
print_date(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 16, 5) # Aquí igual debes definirlo tu

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diferencia = new_year - now
print(diferencia)
diferencia = new_year.date() - current_date # Solo se pueden hacer estas operaciones con el mismo tipo de dato
print(diferencia)

from datetime import timedelta

star_timedelta = timedelta(200, 100, 100, week = 5)
end_timedelta = timedelta(300, 100, 100, week = 10)

print(end_timedelta - star_timedelta)
print(end_timedelta + star_timedelta)

# Timedelta no es para trabajar con fechas sino con franjas de fechas
# diferencia = new_year - now  ## Es hacer esto pero más fácil (creo)