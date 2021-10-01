"""Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

"""

duration = int(input('How long can you have fun in seconds: '))

MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24

if 0 < duration < MIN:
    print(f'{duration // DAY} day {duration % DAY // HOUR} hour {duration % DAY % HOUR // MIN} min'
          f' {duration % MIN} sec?')
    print('Boring...')
elif MIN <= duration < HOUR:
    print(f'{duration // DAY} day {duration % DAY // HOUR} hour {duration % DAY % HOUR // MIN} min'
          f' {duration % MIN} sec?')
    print('Is it enough for you?')
elif HOUR <= duration < DAY:
    print(f'{duration // DAY} day {duration % DAY // HOUR} hour {duration % DAY % HOUR // MIN} min'
          f' {duration % MIN} sec?')
    print('Keep it up!')
elif duration <= 0:
    print(f'What an emo...')
else:
    print(f'{duration // DAY} day {duration % DAY // HOUR} hour {duration % DAY % HOUR // MIN} min'
          f' {duration % MIN} sec?')
    print('Duh! Stop it.')