with open('files.txt', encoding='utf-8') as date:
    files = [i for i in date.readlines()]
    extension = ['.csv', '.exe', '.jpeg', '.json', '.mkv', '.mp3', '.mp4', '.py', '.xml', '.zip']
    weight = []
    for i in extension:
        temp = list(sorted((filter(lambda x: i in x, files))))
        total = 0
        for k in temp:
            if 'KB' in k:
                total += int(k.strip()[k.index(' '):k.rindex(' ')]) * 1024
            if 'MB' in k:
                total += int(k.strip()[k.index(' '):k.rindex(' ')]) * 1024 * 1024
            if 'GB' in k:
                total += int(k.strip()[k.index(' '):k.rindex(' ')]) * 1024 * 1024 * 1024
            if 'B' in k:
                total += int(k.strip()[k.index(' '):k.rindex(' ')])
        if 0.99999 < total / (1024 * 1024 * 1024) < 1024:
            total = f'{round(total / (1024 * 1024 * 1024))} GB'
        elif 0.99999 < total / (1024 * 1024) < 1024:
            total = f'{round(total / (1024 * 1024))} MB'
        elif 0.99999 < total / 1024 < 1024:
            total = f'{round(total / 1024)} KB'
        else:
            total = f'{round(total)} B'
        temp = list(sorted(map(lambda x: x[:x.index(' ')], (filter(lambda x: i in x, files)))))
        print(*temp, '----------', f'Summary: {total}', '', sep='\n')
    # files = sorted(files, key=lambda x: x[x.index('.'):x.index('.')+3])
    # csv = list(sorted(filter(lambda x: '.csv' in x, files)))
    # exe = list(sorted(filter(lambda x: '.exe' in x, files)))
    # jpeg = list(sorted(filter(lambda x: '.jpeg' in x, files)))
    # json = list(sorted(filter(lambda x: '.json' in x, files)))
    # mkv = list(sorted(filter(lambda x: '.mkv' in x, files)))
    # mp3 = list(sorted(filter(lambda x: '.mp3' in x, files)))
    # mp4 = list(sorted(filter(lambda x: '.mp4' in x, files)))
    # py = list(sorted(filter(lambda x: '.py' in x, files)))
    # xml = list(sorted(filter(lambda x: '.xml' in x, files)))
    # zip1 = list(sorted(filter(lambda x: '.zip' in x, files)))
