import csv

def csv_saver(data):
    with open('data/quotes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            'Quote', 'Author'
        )
    
    with open('data/quotes.csv', 'a') as file:
        for quote in data:
            writer.writerow(
                quote
            )