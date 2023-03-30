from datetime import datetime
def choose_plural(amount, declensions):
    if amount > 10:
        if (amount % 10) == 1 and str(amount)[-2] != '1':
            res = f'{amount} {declensions[0]}'
        elif amount % 10 in range(2, 5) and str(amount)[-2] != '1':
            res = f'{amount} {declensions[1]}'
        else:
            res = f'{amount} {declensions[2]}'
    else:
        if (amount % 10) == 1:
            res = f'{amount} {declensions[0]}'
        elif amount % 10 in range(2, 5):
            res = f'{amount} {declensions[1]}'
        else:
            res = f'{amount} {declensions[2]}'
    return res
start_stud, now = datetime(2022, 11, 8, 12), datetime.strptime(input(), '%d.%m.%Y %H:%M')
delta, f = (start_stud - now), 'До выхода курса осталось: '
dayss, hourss, minutss = ("день", "дня", "дней"), ("час", "часа", "часов"), ("минута", "минуты", "минут")
if delta.days > 0:
    f += choose_plural(delta.days, dayss)
    if delta.seconds > 0:
        f += ' и ' + choose_plural(delta.seconds // 3600, hourss)
elif delta.days == 0:
    if delta.seconds // 3600 > 0:
        f += choose_plural(delta.seconds // 3600, hourss)
        if delta.seconds % 3600/60 > 0:
            f += ' и ' + choose_plural(delta.seconds %3600//60, minutss)
    elif delta.seconds % 3600/60 > 0:
        f += choose_plural(delta.seconds % 3600 // 60, minutss)
print(f if f!='До выхода курса осталось: ' else 'Курс уже вышел!')

