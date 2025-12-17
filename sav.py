import webbrowser
import requests
import os
from bs4 import *
import logging
class Sorter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename="my_logg.log",
            filemode="a"
        )
    def sorter(self, url):
        pass
    def website_opening(self, url):
        self.logger.info("відкриття файлу")
        webbrowser.open_new(url)#відкриває обраний сайт
    def storage(self, urll, nam):
        self.logger.info("Запуск функції збереження файлів")
        try:
            response = requests.get(urll)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            nam += ".html"
            with open(nam, "+w", encoding='utf-8') as f:
                f.write(soup.prettify())#зберігає html код обраного сайту
            self.logger.info("фаїл успішно збережено")
            return "сторінку збережено"
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Виникла помилка: {e}")
            return f"помилка при запиті: {e}"
    def opning_a_downloaded_site(self, url):
        self.logger.info("відкриття html фаїл")
        file_path = os.path.abspath(url)#відкриває обраний html код
        URL = 'file://' + file_path
        webbrowser.open(url)
#sort = Sorter()
#url = "C:/Users/DELL/Desktop/program/py/Проекти/http-проект/example_page.html"
#a = sort.opning_a_downloaded_site(url)
#print(a)
