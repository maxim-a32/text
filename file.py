from PyQt5.QtWidgets import *
import sys
import requests
import sav
class http(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scren()
    def scren(self):
        #self.url = 'https://raw.githubusercontent.com/maxim-a32/text/refs/heads/main/text.txt'
        self.screen_size = QApplication.primaryScreen().size()
        self.screen_width = self.screen_size.width()
        self.screen_height = self.screen_size.height()
        self.resize(self.screen_width, self.screen_height)
        self.label = QLabel("ведіть 1 щоб відкрити сторінку з інтернету, 2 щоб зберегти сторінку, 3 щоб вікрити збережену сторінку", self)
        self.button = QPushButton("Кнопка")
        self.line = QLineEdit()
        self.button.clicked.connect(self.file)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        vbox.addWidget(self.line)
        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
    def file(self):
        text = self.line.text()
        if text == "1":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.openn)
            self.label.setText("ведіть url сторінки яку бажаєте відкрити")
        if text == "2":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.namee)
            self.label.setText("ведіть url сторінки яку бажаєте зберегти")
        if text == "3":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.open_sav)
            self.label.setText("ведіть повний шлях до файлу з html кодом який хочете відкрити")
        #try:
            #text = requests.get(self.url)
            #text.raise_for_status()
            #file_content = text.text
            #self.label.setText(file_content)
        #except requests.exceptions.RequestException as e:
            #self.label.setText(f"помилка під час отримання файлу: {e}")
    def openn(self):
        self.url = self.line.text()
        handler.website_opening(self.url)
    def namee(self):
        self.url = self.line.text()
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.savee)
        self.label.setText("ведіть як буде називатися фаїл з html кодом")
    def savee(self):
        nam = self.line.text()
        text = handler.storage(self.url, nam)
        self.label.setText(text)
    def open_sav(self):
        text = self.line.text()
        handler.opning_a_downloaded_site(text)
handler = sav.Sorter()
app = QApplication(sys.argv)
start = http()
start.show()
sys.exit(app.exec_())
        
