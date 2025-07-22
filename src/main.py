from saver import csv_saver
from parser import get_html, parse_quotes
from limit import ask_limit

def main(url: str):
    
    html = get_html(url)
    if html is None:
        print('ERROR: Не удалось получить HTML с сайта')
        return
    
    limit = ask_limit()
            
    data = parse_quotes(html, limit)
    if data:
        csv_saver(data)
        print(f'Успешно сохранено {len(data)} цитат(ы) в файл: "data/quotes.csv"')
    else:
        print("Цитаты не найдены или пустой результат.")
    
if __name__ == '__main__':
    main(url='http://quotes.toscrape.com/')