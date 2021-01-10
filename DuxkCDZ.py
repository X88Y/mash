import time

print('Ваша поддержка - https://www.donationalerts.com/r/duckhack')
print('Можно выделить и скопировать ссылку сверху')
time.sleep(6)
print('Думал пошел прогресс а мне нужны деньги блять')
time.sleep(3)
print('Все еще нужны')
time.sleep(0.5)
print('Credits:')
print('Code by Duxk from 228iQTeam')


from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import json
import sys

notright = []
ready = []
i = 0

var = input('Вставте вариант. После замените ссылки на содержимое из них\n>')

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.textEdit.setPlainText('https://uchebnik.mos.ru/exam/rest/secure/api/answer/variant/' + var)
ui.textEdit_2.setPlainText('https://uchebnik.mos.ru/exam/rest/secure/api/task/variant/' + var)

def cdz(raw, raw2_json, question, pos):
    for task in raw:
        if task['is_right'] == pos:
            MathPart = ' '
            if task['given_answer']['@answer_type'] == 'answer/single':
                if task['task_id'] not in ready:
                    MathPart = ' '
                    temp = (task['given_answer']['id'])
                    task_id = task['task_id']
                    ready.append(task_id)
                    for search in question:  # вопрос
                        if search['id'] == task_id:  #
                            print('Задание№', search['taskNum'])  #
                            try:
                                print('Вопрос:', search['question_elements'][0]['text'])  #
                            except:
                                print('Вопрос:', search['question_elements'][0]['relative_url'])
                    Letteranswer = raw2_json.split(temp)[1].split('content')[0][10:-3]
                    try:
                        MathPart = ''
                        MathPart = raw2_json.split(temp)[1].split('"taskNum":')[0].split('is_multiline')[0]
                        MathPart = MathPart.split('"content":"')[1][0:-3]
                        print('>' + Letteranswer+ MathPart)
                    except:
                        print('>' + Letteranswer)


            elif task['given_answer']['@answer_type'] == "answer/multiple":
                if task['task_id'] not in ready:
                    temp = task['given_answer']['ids']
                    task_id = task['task_id']
                    ready.append(task_id)
                    for search in question:
                        if search['id'] == task_id:
                            print('Задание№', search['taskNum'])
                            print(search['question_elements'][0]['text'])
                    for i in temp:
                        Letteranswer = raw2_json.split(i)[1].split('content')[0][10:-3]
                        print('>' + Letteranswer)

    if len(ready) < 3:
        ready.append('Null')
        print('Эти ответы не точные, ибо учитель их еще не проверил')
        cdz(raw, raw2_json, question, None)

def main():
    raw = json.loads(ui.textEdit.toPlainText())
    raw2_json = ui.textEdit_2.toPlainText()
    question = json.loads(ui.textEdit_2.toPlainText())
    cdz(raw, raw2_json, question, True)
    print('Версия 1.4.0')

ui.pushButton.clicked.connect(main)
sys.exit(app.exec_())
