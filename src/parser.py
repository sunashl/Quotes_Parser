import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114 Safari/537.36"
}

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

    