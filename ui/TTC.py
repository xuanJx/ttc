import sys

from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.TTC_UI import Ui_Form
from ui.url_ttc import Ttc_Price

font_command = QFont()
font_command.setFamily("Arial")
#font_command.setFamily("宋体")
font_command.setPointSize(8)

num = ''
minprice = ''
hightprice = ''

class TTC_wi(QWidget, Ui_Form):
    def __init__(self):
        super(TTC_wi, self).__init__()
        self.setupUi(self)

        self.pattern = ''
        self.only_motif_raido.setChecked(True)
        self.pushButton.clicked.connect(self.pushButton_A)
        self.only_motif_raido.clicked.connect(self.pattern_motif)
        self.not_noly_motif_radio.clicked.connect(self.pattern_motif)

    @pyqtSlot()
    def pattern_motif(self):
        if self.only_motif_raido.isChecked():
            self.pattern = 'only_motif'
            self.num_line_edit_not_motif.setDisabled(True)
            self.num_line_edit.setDisabled(False)
        elif self.not_noly_motif_radio.isChecked():
            self.pattern = 'not_only_motif'
            self.num_line_edit.setDisabled(True)
            self.num_line_edit_not_motif.setDisabled(False)

    @pyqtSlot()
    def pushButton_A(self):
        global num, minprice, hightprice
        if self.pattern == 'only_motif':
            num = self.num_line_edit.text()
        elif self.pattern == 'not_only_motif':
            num = self.num_line_edit_not_motif.text()

        minprice = self.min_price_line.text()
        hightprice = self.hight_price_line.text()

        if not num:
            QMessageBox.about(self, '没有输入风格页编号', '请输入风格页编号！ ')
            return

        if not minprice:
            minprice = str(0)

        if not hightprice:
            hightprice = str(9999999)

        # if not num.isdigit():
        #     QMessageBox.about(self, '风格页编号错误', '请输入数字！ ')
        #     return

        if not hightprice.isdigit():
            QMessageBox.about(self, '价格错误', '请输入数字！ ')
            return

        if not minprice.isdigit():
            QMessageBox.about(self, '价格错误', '请输入数字！ ')
            return

        if int(num) > 94:
            QMessageBox.about(self, '风格页编号错误', '目前最高到94风格页！ ')
            return

        self.pushButton.setDisabled(True)
        if self.pattern == 'only_motif':
            thre = Run_thr()
            thre.signal_data.connect(self.Main)
            thre.start()
            thre.exec()
        elif self.pattern == 'not_only_motif':
            thre = Run_thrA()
            thre.signal_data.connect(self.Main)
            thre.start()
            thre.exec()

    def Main(self, b):

        # for i in range(10):
        #     list = b[i]
        #     self.time_one.setText(list[0])
        #     self.name_one.setText(list[1])
        #     self.place_one.setText(list[2])
        #     self.single_one.setText(list[3])
        #     self.total_one.setText(list[4])

        list1 = b[0]
        list2 = b[1]
        list3 = b[2]
        list4 = b[3]
        list5 = b[4]
        list6 = b[5]
        list7 = b[6]
        list8 = b[7]
        list9 = b[8]
        list10 = b[9]

        self.time_one.setText(self.list1[0])
        self.name_one.setText(self.list1[1])
        self.place_one.setText(self.list1[2])
        self.single_one.setText(self.list1[3])
        self.total_one.setText(self.list1[4])

        self.time_two.setText(self.list2[0])
        self.name_two.setText(self.list2[1])
        self.place_two.setText(self.list2[2])
        self.single_two.setText(self.list2[3])
        self.total_two.setText(self.list2[4])

        self.time_three.setText(self.list3[0])
        self.name_three.setText(self.list3[1])
        self.place_three.setText(self.list3[2])
        self.single_three.setText(self.list3[3])
        self.total_three.setText(self.list3[4])

        self.time_four.setText(self.list4[0])
        self.name_four.setText(self.list4[1])
        self.place_four.setText(self.list4[2])
        self.single_four.setText(self.list4[3])
        self.total_four.setText(self.list4[4])

        self.time_five.setText(self.list5[0])
        self.name_five.setText(self.list5[1])
        self.place_five.setText(self.list5[2])
        self.single_five.setText(self.list5[3])
        self.total_five.setText(self.list5[4])

        self.time_six.setText(self.list6[0])
        self.name_six.setText(self.list6[1])
        self.place_six.setText(self.list6[2])
        self.single_six.setText(self.list6[3])
        self.total_six.setText(self.list6[4])

        self.time_seven.setText(self.list7[0])
        self.name_seven.setText(self.list7[1])
        self.place_seven.setText(self.list7[2])
        self.single_seven.setText(self.list7[3])
        self.total_seven.setText(self.list7[4])

        self.time_eight.setText(self.list8[0])
        self.name_eight.setText(self.list8[1])
        self.place_eight.setText(self.list8[2])
        self.single_eight.setText(self.list8[3])
        self.total_eight.setText(self.list8[4])

        self.time_nine.setText(self.list9[0])
        self.name_nine.setText(self.list9[1])
        self.place_nine.setText(self.list9[2])
        self.single_nine.setText(self.list9[3])
        self.total_nine.setText(self.list9[4])

        self.time_ten.setText(self.list10[0])
        self.name_ten.setText(self.list10[1])
        self.place_ten.setText(self.list10[2])
        self.single_ten.setText(self.list10[3])
        self.total_ten.setText(self.list10[4])

        self.pushButton.setDisabled(False)

        if self.pattern == 'only_motif':
            self.num_line_edit.setDisabled(False)
        elif self.pattern == 'not_only_motif':
            self.num_line_edit_not_motif.setDisabled(False)

    def split_list(self):
        self.list1 = b[0]
        self.list2 = b[1]
        self.list3 = b[2]
        self.list4 = b[3]
        self.list5 = b[4]
        self.list6 = b[5]
        self.list7 = b[6]
        self.list8 = b[7]
        self.list9 = b[8]
        self.list10 = b[9]


class Run_thr(QThread):
    signal_data = pyqtSignal(list)

    def __init__(self):
        super(Run_thr, self).__init__()

    def run(self):
        a = Ttc_Price(num, minprice, hightprice, motif=True)
        self.signal_data.emit(a.New_Soup())

class Run_thrA(QThread):
    signal_data = pyqtSignal(list)

    def __init__(self):
        super(Run_thrA, self).__init__()

    def run(self):
        a = Ttc_Price(num, minprice, hightprice, motif=None)
        self.signal_data.emit(a.New_Soup())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    TTC = TTC_wi()
    TTC.show()
    sys.exit(app.exec_())