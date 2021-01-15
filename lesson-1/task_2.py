user_time = int(input('Input time in seconds: '))
hours = int(user_time / 60 // 60)
if hours < 10:
    str_hours = '0'
else:
    str_hours = ''
minutes = int(user_time / 60 % 60)
if minutes < 10:
    str_minutes = '0'
else:
    str_minutes = ''
seconds = int(user_time % 60)
if seconds < 10:
    str_seconds = '0'
else:
    str_seconds = ''

print(f'{str_hours}{hours}:{str_minutes}{minutes}'
      f':{str_seconds}{seconds}')
