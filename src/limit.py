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