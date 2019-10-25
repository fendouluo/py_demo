#!/usr/bin/env python3
days = int(input('Enter days:'))
print('Months = {} Days = {}'.format(*divmod(days,30)))
months = days // 30
days = days % 30
print('Months = {} Days = {}'.format(months, days))
