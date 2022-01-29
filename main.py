import requests
import bs4
from logger import logger


@logger('log_path','log.csv')
def wheather (city):
    try:
        result_dict = {'city':'', 'temp': '', 'desc':''}
        response = requests.get(f'https://sinoptik.com.ru/погода-{city.lower()}')
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, features='html.parser')
        div = soup.find_all('div', class_='weather__content_tab current dateFree')
        for item in div:
            temp = item.find('b')
            temp1 = temp.find_next('b')
            desc = item.find('label', class_='show-tooltip').text
        result_dict['city'] = city.capitalize()
        result_dict['temp'] = str(f'{temp.text} {temp1.text}')
        result_dict['desc'] = desc.replace('\n','')
        return result_dict
    except:
        return ("You'r input wrong sity")
w = wheather('москва')

