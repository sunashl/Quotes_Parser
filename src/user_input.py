from saver import csv_saver, json_saver

def ask_limit():
    
    while True:
        try:
            limit = int(input('Введите количество цитат:'))
            if 1 <= limit <= 10:
                break
            else:
                print('ERROR: Введите число от 1 до 10')
        except ValueError:
            print('ERROR: Введите корректное число')
    
    return limit


def ask_format():
    
    while True:
        try:
            format = str(input('Введите формат сохранения:'))
            if format.lower().strip() in ['json', 'csv']:
                if format.lower().strip() == 'csv':
                    return csv
                    break
                elif format.lower().strip() == 'json':
                    return json
                    break
            else:
                print('ERROR: Введите формат сохранения')
        except Exception:
            print('ERROR: Введите корректный формат')
    return