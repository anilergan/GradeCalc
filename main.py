from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator
from qt import Ui_MainWindow


# pyinstaller --onefile -w -i qualifications.ico main.py

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # signal slots
        self.ui.dial_final_note_vize1.valueChanged.connect(self.show_final_note_vize1_percent)
        self.ui.dial_final_note_vize2.valueChanged.connect(self.show_final_note_vize2_percent)
        self.ui.dial_note_avr_vize1.valueChanged.connect(self.show_note_avr_vize1_percent)
        self.ui.dial_note_avr_vize2.valueChanged.connect(self.show_note_avr_vize2_percent)
        self.ui.button_final_note.clicked.connect(self.final_note_process)
        self.ui.button_note_avr.clicked.connect(self.note_avr_process)
        self.ui.button_clear.clicked.connect(self.clear_process)
        self.ui.lineedit_final_note_vize1.textChanged.connect(self.check_lineedit_fnv1)
        self.ui.lineedit_final_note_vize2.textChanged.connect(self.check_lineedit_fnv2)
        self.ui.lineedit_note_avr_vize1.textChanged.connect(self.check_lineedit_nav1)
        self.ui.lineedit_note_avr_vize2.textChanged.connect(self.check_lineedit_nav2)
        self.ui.lineedit_note_avr_final.textChanged.connect(self.check_lineedit_naf)
        self.myValidators()



    def check_lineedit_fnv1(self):
        try:
            int(self.ui.lineedit_final_note_vize1.text()) 
        except: 
            return None
        
        if int(self.ui.lineedit_final_note_vize1.text()) > 100 :
            self.ui.lineedit_final_note_vize1.setStyleSheet(
"border: 2px dotted red;\n"
"color: red;")
        else: self.ui.lineedit_final_note_vize1.setStyleSheet("")
    
    
    def check_lineedit_fnv2(self):
        try:
            int(self.ui.lineedit_final_note_vize2.text()) 
        except: 
            return None
        
        if int(self.ui.lineedit_final_note_vize2.text()) > 100 :
            self.ui.lineedit_final_note_vize2.setStyleSheet(
"border: 2px dotted red;\n"
"color: red;")
        else: self.ui.lineedit_final_note_vize2.setStyleSheet("")
    
    def check_lineedit_nav1(self):
        try:
            int(self.ui.lineedit_note_avr_vize1.text()) 
        except: 
            return None
        
        if int(self.ui.lineedit_note_avr_vize1.text()) > 100 :
            self.ui.lineedit_note_avr_vize1.setStyleSheet(
"border: 2px dotted red;\n"
"color: red;")
        else: self.ui.lineedit_note_avr_vize1.setStyleSheet("")
    
    
    def check_lineedit_nav2(self):
        try:
            int(self.ui.lineedit_note_avr_vize2.text()) 
        except: 
            return None
        
        if int(self.ui.lineedit_note_avr_vize2.text()) > 100 :
            self.ui.lineedit_note_avr_vize2.setStyleSheet(
"border: 2px dotted red;\n"
"color: red;")
        else: self.ui.lineedit_note_avr_vize2.setStyleSheet("")
    
    
    def check_lineedit_naf(self):
        try:
            int(self.ui.lineedit_note_avr_final.text()) 
        except: 
            return None
        
        if int(self.ui.lineedit_note_avr_final.text()) > 100 :
            self.ui.lineedit_note_avr_final.setStyleSheet(
"border: 2px dotted red;\n"
"color: red;")
        else: self.ui.lineedit_note_avr_final.setStyleSheet("")



    def clear_process(self):
        self.ui.dial_final_note_vize1.setValue(6)
        self.ui.dial_final_note_vize2.setValue(6)
        self.ui.dial_note_avr_vize1.setValue(6)
        self.ui.dial_note_avr_vize2.setValue(6)
        self.ui.show_note_avr_percent_final.setText('40')
        self.show_final_note_vize1_percent()
        self.show_final_note_vize2_percent()
        self.show_note_avr_vize1_percent()
        self.show_note_avr_vize2_percent()
        self.ui.lineedit_note_avr_vize1.clear()
        self.ui.lineedit_note_avr_vize2.clear()
        self.ui.lineedit_note_avr_final.clear()
        self.ui.lineedit_final_note_vize1.clear()
        self.ui.lineedit_final_note_vize2.clear()
        self.ui.show_calc_final_note.clear()
        self.ui.show_calc_note_avr.clear()
        self.ui.groupbox_final_note.setStyleSheet("")
        self.ui.groupbox_note_avr.setStyleSheet("")
        self.ui.lineedit_final_note_vize1.setStyleSheet("")
        self.ui.lineedit_final_note_vize2.setStyleSheet("")
        self.ui.lineedit_note_avr_vize1.setStyleSheet("")
        self.ui.lineedit_note_avr_vize2.setStyleSheet("")
        self.ui.lineedit_note_avr_final.setStyleSheet("")




    def show_final_note_vize1_percent(self):
        self.ui.show_final_note_percent_vize1.setText(str(self.ui.dial_final_note_vize1.value() * 5))
        
        if int(self.ui.show_final_note_percent_vize1.text()) + int(self.ui.show_final_note_percent_vize2.text()) > 100:
            self.ui.warning_final_note.setText("Yüzdelik girişi geçersiz!")
        else: 
            self.ui.warning_final_note.setText("")

    def show_final_note_vize2_percent(self):
        self.ui.show_final_note_percent_vize2.setText(str(self.ui.dial_final_note_vize2.value() * 5))
        
        if int(self.ui.show_final_note_percent_vize1.text()) + int(self.ui.show_final_note_percent_vize2.text()) > 100:
            self.ui.warning_final_note.setText("Yüzdelik girişi geçersiz!")
        else: 
            self.ui.warning_final_note.setText("")

    def show_note_avr_vize1_percent(self):
        self.ui.show_note_avr_percent_vize1.setText(str(self.ui.dial_note_avr_vize1.value() * 5))
        self.remain_percent = 100 - ((self.ui.dial_note_avr_vize1.value() * 5) + (self.ui.dial_note_avr_vize2.value() * 5))
        if self.remain_percent >= 0:
            self.ui.show_note_avr_percent_final.setText(str(self.remain_percent))
        else: 
            self.ui.show_note_avr_percent_final.setText("-")

        if self.ui.show_note_avr_percent_final.text() == '-':
            self.ui.warning_note_avr.setText("Yüzdelik girişi geçersiz!")
        else: 
            self.ui.warning_note_avr.setText("")
        

    def show_note_avr_vize2_percent(self):
        self.ui.show_note_avr_percent_vize2.setText(str(self.ui.dial_note_avr_vize2.value() * 5))
        self.remain_percent = 100 - ((self.ui.dial_note_avr_vize1.value() * 5) + (self.ui.dial_note_avr_vize2.value() * 5))
        if self.remain_percent >= 0:
            self.ui.show_note_avr_percent_final.setText(str(self.remain_percent))
        else: 
            self.ui.show_note_avr_percent_final.setText("-")

        if self.ui.show_note_avr_percent_final.text() == '-':
            self.ui.warning_note_avr.setText("Yüzdelik girişi geçersiz!")
        else: 
            self.ui.warning_note_avr.setText("")
        


    def final_note_process(self):

        if self.ui.warning_final_note.text() == "Yüzdelik girişi geçersiz!":
            return None

        elif (self.ui.lineedit_final_note_vize2.text() == '') | (self.ui.lineedit_final_note_vize1.text() == ''):
            self.ui.warning_final_note.setText('Not girişi eksik!')
            return None    
        
        elif (int(self.ui.lineedit_final_note_vize2.text()) > 100) | (int(self.ui.lineedit_final_note_vize1.text()) > 100):
            self.ui.warning_final_note.setText('Not girişi geçersiz!')
            return None   
        else: 
            self.ui.warning_note_avr.setText("")


        self.final_note = self.calc_final_note(
            int(self.ui.lineedit_final_note_vize1.text()),
            int(self.ui.lineedit_final_note_vize2.text()),
            int(self.ui.show_final_note_percent_vize1.text()),
            int(self.ui.show_final_note_percent_vize2.text()))

        self.ui.show_calc_final_note.setText(str(self.final_note))

        if self.final_note < 25.0:
            self.ui.groupbox_final_note.setStyleSheet(
"#groupbox_final_note{\n"
"background-color: rgb(50,255,0,30);\n"
"border: 1px solid rgb(50,255,0,200);}\n"
"#show_calc_final_note{\n"
"background-color: rgb(50,255,0,20);\n"
"border: 2px solid rgb(50,255,0);}"
)
            

        elif self.final_note <= 40.0:
            self.ui.groupbox_final_note.setStyleSheet(
"#groupbox_final_note{"
"background-color: rgb(255,230,0,30);\n"
"border: 1px solid rgb(255,230,0,200);}\n"
"#show_calc_final_note{\n"
"background-color: rgb(255,230,0,20);\n"
"border: 2px solid rgb(255,230,0);}"
)


        else:
            self.ui.groupbox_final_note.setStyleSheet(
"#groupbox_final_note{"
"background-color: rgb(255,50,0,30);\n"
"border: 1px solid rgb(255,50,0,200);}\n"
"#show_calc_final_note{\n"
"background-color: rgb(255,50,0,20);\n"
"border: 2px solid rgb(255,50,0);}"
)

        
        if self.final_note > 0:
            self.ui.show_calc_final_note.setText(str(self.final_note))
        
        else: 
            self.ui.show_calc_final_note.setText('Passed')


    def note_avr_process(self):
        if self.ui.warning_note_avr.text() == "Yüzdelik girişi geçersiz!":
            return None

        elif (self.ui.lineedit_note_avr_final.text() == '') | (self.ui.lineedit_note_avr_vize1.text() == '') | (self.ui.lineedit_note_avr_vize2.text() == ''):
            self.ui.warning_note_avr.setText('Not girişi eksik!')
            return None    
        
        elif (int(self.ui.lineedit_note_avr_final.text()) > 100) | (int(self.ui.lineedit_note_avr_vize1.text()) > 100) | (int(self.ui.lineedit_note_avr_vize2.text()) > 100):
            self.ui.warning_note_avr.setText('Not girişi geçersiz!')
            return None
        
        else: 
            self.ui.warning_note_avr.setText("")

        self.note_avr = self.calc_note_avr(
            int(self.ui.lineedit_note_avr_vize1.text()),
            int(self.ui.lineedit_note_avr_vize2.text()),
            int(self.ui.show_note_avr_percent_vize1.text()),
            int(self.ui.show_note_avr_percent_vize2.text()),
            int(self.ui.lineedit_note_avr_final.text()))
            
        self.ui.show_calc_note_avr.setText(str(self.note_avr))


        if self.note_avr < 40.0:
            self.ui.groupbox_note_avr.setStyleSheet(
"#groupbox_note_avr{\n"
"background-color: rgb(255,50,0,30);\n"
"border: 1px solid rgb(255,50,0,200);}\n"
"#show_calc_note_avr{\n"
"background-color: rgb(255,50,0,20);\n"
"border: 2px solid rgb(255,50,0);}"
)


        elif self.note_avr < 60.0:
            self.ui.groupbox_note_avr.setStyleSheet(
"#groupbox_note_avr{\n"
"background-color: rgb(255,230,0,30);\n"
"border: 1px solid rgb(255,230,0,200);}\n"
"#show_calc_note_avr{\n"
"background-color: rgb(255,230,0,20);\n"
"border: 2px solid rgb(255,230,0);}"
)


        elif self.note_avr >= 60.0:
            self.ui.groupbox_note_avr.setStyleSheet(
"#groupbox_note_avr{\n"
"background-color: rgb(50,255,0,30);\n"
"border: 1px solid rgb(50,255,0,200);}\n"
"#show_calc_note_avr{\n"
"background-color: rgb(50,255,0,20);\n"
"border: 2px solid rgb(50,255,0);}"
)
        

    def calc_final_note(self, v1, v2, p1, p2):

        self.pass_mark = 40
        self.final_percent = (100 - (p1 + p2)) / 100
        self.final_note = (self.pass_mark - ((v1 * p1/100) + (v2 * p2/100))) / self.final_percent

        return int(self.final_note)



    def calc_note_avr(self, v1, v2, p1, p2, f):
        self.final_percent = (100 - (p1 + p2))
        note_avr = (v1*p1 + v2*p2 + f*self.final_percent)/100
        return note_avr


    def myValidators(self):
        self.validator = QIntValidator(0,100,self)
        self.ui.lineedit_final_note_vize1.setValidator(self.validator)
        self.ui.lineedit_final_note_vize2.setValidator(self.validator)
        self.ui.lineedit_note_avr_vize1.setValidator(self.validator)
        self.ui.lineedit_note_avr_vize2.setValidator(self.validator)
        self.ui.lineedit_note_avr_final.setValidator(self.validator)
        



def runApp():
    app = QApplication([])
    win = myWindow()
    win.show()
    app.exec_()

runApp()