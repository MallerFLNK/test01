from main_window import *
from PyQt5.QtWidgets import QApplication, QWidget
from random import shuffle
card_width, card_height = 600,500

app = QApplication([])

window.resize(card_width,card_height)
window.move(300,300)
window.setWindowTitle("Memory Card")
text_wrong = "Wrong"
text_correc = "Well done!" #good,correct

frm_question = 'Яблуко'
frm_right = "apple"
frm_wrong1 = "application"
frm_wrong2 = "pear"
frm_wrong3 = "grape"

radio_list = [rbtn_ans1,rbtn_ans2,rbtn_ans3,rbtn_ans4]

shuffle(radio_list)

answer = radio_list[0]
wrong_answer = radio_list[1]
wrong_answer = radio_list[2]
wrong_answer = radio_list[3]



window.show()
app.exec_()