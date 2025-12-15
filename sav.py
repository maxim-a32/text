import webbrowser
import requests
import os
from bs4 import *
class Sorter:
    def sorter(self, url):
        pass
    def website_opening(self, url):
        webbrowser.open_new(url)#відкриває обраний сайт
    def storage(self, urll, nam):
        try:
            response = requests.get(urll)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            nam += ".html"
            with open(nam, "+w", encoding='utf-8') as f:
                f.write(soup.prettify())#зберігає html код обраного сайту
            return "сторінку збережено"
        except requests.exceptions.RequestException as e:
            print(e)
            return f"помилка при запиті: {e}"
    def opning_a_downloaded_site(self, url):
        file_path = os.path.abspath(url)#відкриває обраний html код
        URL = 'file://' + file_path
        webbrowser.open(url)
#sort = Sorter()
#url = "C:/Users/DELL/Desktop/program/py/Проекти/http-проект/example_page.html"
#a = sort.opning_a_downloaded_site(url)
#print(a)
