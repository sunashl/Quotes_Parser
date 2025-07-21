import requests
from bs4 import BeautifulSoup
from config import headers, classes

def get_html(url): 
    try:
        response = requests.get(url, headers=headers, timeout=(3, 5))
        response.raise_for_status()
        return response.text
    
    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error: {e.response.status_code} - {e.response.reason}')
    except requests.exceptions.ConnectionError:
        print('Connection Error: Check the Internet or URL')
    except requests.exceptions.Timeout:
        print('Timeout Error: The server did not respond in time')
    except requests.exceptions.RequestException as e:
        print(f'Unknown Error: {e}')
        
    return None


def get_links(html):
    soup = BeautifulSoup(html, 'lxml')
    
    links = soup.find_all('a', class_=classes["links"])
    all_vacancy_links = {}
    
    for vacancy in links:
        vacancy_title = vacancy.text
        vacancy_link = vacancy.get('href')
        
        all_vacancy_links[vacancy_title] = vacancy_link
    return all_vacancy_links


