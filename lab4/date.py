import datetime

# task 1
now = datetime.datetime.now()
now -= datetime.timedelta(days=5)
print(now)

# task 2
now = datetime.datetime.now()
ys = now - datetime.timedelta(days=1)
tmr = now + datetime.timedelta(days=1)
print(f'yesterday: {ys.strftime("%y-%m-%d")}, today: {now.strftime("%y-%m-%d")}, tomorrow: {tmr.strftime("%y-%m-%d")}')

# task 3
def drop_ms(date: datetime.datetime):
    return date.replace(microsecond=0)

now = datetime.datetime.now()
print(f'pre-drop {now}')
now = drop_ms(now)
print(f'dropped {now}')

# task 4
def diff(date1, date2: datetime.datetime):
    delta = date2 - date1
    return delta.seconds

now = datetime.datetime.now()
future = now + datetime.timedelta(seconds=50)
print(f'difference is {diff(now, future)} seconds')
