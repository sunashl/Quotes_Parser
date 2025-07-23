from parser import get_html, parse_quotes
from user_input import ask_limit, ask_format
from saver import csv_saver, json_saver

def main(url: str):
    
    html = get_html(url)
    if html is None:
        print('ERROR: Не удалось получить HTML с сайта')
        return
    
    limit = ask_limit()
            
    data = parse_quotes(html, limit)
    if data:
        format = ask_format()
        if format == 'csv':
            csv_saver(data)
            print(f'Успешно сохранено {len(data)} цитат(ы) в файл "data/quotes.csv"')
        elif format == 'json':
            json_saver(data)
            print(f'Успешно сохранено {len(data)} цитат(ы) в файл "data/quotes.json"')
    else:
        print("Цитаты не найдены или пустой результат.")
    
if __name__ == '__main__':
    main(url='http://quotes.toscrape.com/')