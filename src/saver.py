import csv

def csv_saver(data):
    with open('data/quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            ('Quote', 'Author', 'Tags')
        )
        for quote in data:
            tags_str = ', '.join(quote['tags'])
            writer.writerow(
                (quote['quote'], quote['author'], tags_str)
            )