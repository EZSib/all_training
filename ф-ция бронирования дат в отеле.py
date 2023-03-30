from datetime import datetime, timedelta
def convers(dates):
    date_set = []
    for i in dates:
        temp = []
        if len(i) > 10:
            i = i.split('-')
            for j in i:
                temp.append(datetime.strptime(j, '%d.%m.%Y'))
        else:
            date_set.append((datetime.strptime(i, '%d.%m.%Y')))
        if len(temp) > 0:
            delta = max(temp) - min(temp)
            for m in range(delta.days + 1):
                date_set.append(min(temp) + timedelta(m))
    return set(date_set)
def convers1(some_date):
    some_date_set = []
    temp = []
    if len(some_date) > 11:
        some_date = some_date.split('-')
        for j in some_date:
            temp.append(datetime.strptime(j, '%d.%m.%Y'))
    else:
        some_date_set.append((datetime.strptime(some_date, '%d.%m.%Y')))
    if len(temp) > 0:
        delta = max(temp) - min(temp)
        for m in range(delta.days + 1):
            some_date_set.append(min(temp) + timedelta(m))
    return set(some_date_set)
def is_available_date(dates, some_date):
    return convers(dates).isdisjoint(convers1(some_date))
print(is_available_date(dates, some_date))

