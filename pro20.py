import webbrowser
from random import randint #

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QIcon #

def get_barbi():
    return webbrowser.open('https://www.kinopoisk.ru/film/478052/?utm_referrer=www.google.com')

def get_random_film(): #
    if len(lst_films) > 0: #
        url = lst_films[randint(0, len(lst_films)-1)] #
        lst_films.remove(url) #
        return webbrowser.open(url) #
    else: #
        box = QMessageBox() #
        box.setText('Фильмов больше\nне осталось!!!') #
        box.exec() #

lst_films = [ #
    'https://www.kinopoisk.ru/film/478052/?utm_referrer=www.google.com', #
    'https://www.kinopoisk.ru/film/937438/?utm_referrer=www.google.com', #
    "https://www.kinopoisk.ru/film/762738/", #
    "https://www.kinopoisk.ru/film/507/" #
] #

app = QApplication([])
window = QWidget()
window.setFixedSize(400,250)
window.setWindowTitle('Кинопоиск')

line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()

text = QLabel('Выберите фильм:')
btn1 = QPushButton('Барби')
btn2 = QPushButton('2')
btn3 = QPushButton('3')
btn4 = QPushButton('4')
btn5 = QPushButton('Рандом') #

btn1.clicked.connect(get_barbi)
btn5.clicked.connect(get_random_film) #

line_h1.addWidget(btn1, alignment=Qt.AlignCenter)
line_h1.addWidget(btn2, alignment=Qt.AlignCenter)
line_h2.addWidget(btn3, alignment=Qt.AlignCenter)
line_h2.addWidget(btn4, alignment=Qt.AlignCenter)
line_h3.addWidget(btn5, alignment=Qt.AlignCenter) #

line.addWidget(text, alignment=Qt.AlignCenter)
line.addLayout(line_h1)
line.addLayout(line_h2)
line.addLayout(line_h3) #

window.setStyleSheet('background-color: rgb(255,0,0); color:white; font-size:25px; font-style:italic; font-weight: 900')
btn1.setStyleSheet('background-color: rgb(255,0,255); border: 10px double orange')
text.setStyleSheet('border: 10px double orange')
# text.setFont(QFont('Times New Roman'))


window.setWindowIcon(QIcon('kino.ico')) #
window.setLayout(line)
window.show()
app.exec()