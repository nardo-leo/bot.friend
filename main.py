import requests
from bs4 import BeautifulSoup


class ParserBolshoi:

    def __init__(self, start_url):
        self.start_url = start_url

    def _get(self, url) -> BeautifulSoup:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def run(self) -> str:
        soup = self._get(self.start_url)
        answer = self.parse(soup)
        print(self.answer(answer))

    def parse(self, soup) -> str:
        text_block = soup.find('div', attrs={'class', 'text_content_block'})
        return text_block.find_all('a')[25].text

    def answer(self, current_text: str):
        december_text = 'График продажи билетов на НОЯБРЬ и ДЕКАБРЬ 2020 г.\n\t\t\t с учетом ограничения посетителей до 25% вместимости зрительного зала'
        if (current_text != december_text):
            return f'Time to buy tickets {self.start_url}'\
                   f'[Nutcracker in Bolshoi]'
        else:
            return f'Nothing changed [Nutcracker in Bolshoi]'


if __name__ == '__main__':
    url = 'https://www.bolshoi.ru/visit/buyingnew/'
    parser = ParserBolshoi(url)
    parser.run()
