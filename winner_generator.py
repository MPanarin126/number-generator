from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

#создание элементов интерфейса
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
#название окна
button =QPushButton('Сгенерировать')
#кнопка сгененрировать
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')
#текст

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
main_win.resize(600, 300)
main_win.move(450,120)

#привязка элементов к вертикальной линии
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

button.clicked.connect(show_winner)

main_win.show()
app.exec_()
#обработка событий

#запуск приложения