import requests
from bs4 import BeautifulSoup


url = 'https://www.bolshoi.ru/visit/buyingnew/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

dec_text = 'График продажи билетов на НОЯБРЬ и ДЕКАБРЬ 2020 г.\n\t\t\t с учетом ограничения посетителей до 25% вместимости зрительного зала'
text_block = soup.find('div', attrs={'class', 'text_content_block'})
a = text_block.find_all('a')[25]
cur_text = a.text

if (cur_text != dec_text):
    # send_message
