from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random


class MyTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = QTableWidget(parent)
        self._mainwin = parent

        self.__make_layout()
        self.__make_table()

    def __make_table(self):
        # self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        # setting number of row, column
        self.table.setColumnCount(5)
        self.table.setRowCount(3)

        # naming column header
        self.table.setHorizontalHeaderLabels(["code", "name"])
        self.table.horizontalHeaderItem(0).setToolTip("code...")  # header tooltip
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)

        header_item = QTableWidgetItem("add")
        header_item.setBackground(Qt.red)  # background color of header
        self.table.setHorizontalHeaderItem(2, header_item)



        # entering data into cell
        self.table.setItem(0, 0, QTableWidgetItem("000020"))
        self.table.setItem(0, 1, QTableWidgetItem("Hyatts Hotel"))
        self.table.setItem(1, 0, QTableWidgetItem("000030"))
        self.table.setItem(1, 1, QTableWidgetItem("Euroceramic"))
        self.table.setItem(2, 0, QTableWidgetItem("000080"))
        item = QTableWidgetItem("Duomo")
        self.table.setItem(2, 1, item)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table.setColumnWidth(2, 50)
        ckbox = QCheckBox()
        self.table.setCellWidget(0, 2, ckbox)
        ckbox2 = QCheckBox('me')
        self.table.setCellWidget(1, 2, ckbox2)

        mycom = QComboBox()
        mycom.addItems(["aa", "dd", "kk"])
        mycom.addItem("cc")
        mycom.addItem("bb")
        self.table.setCellWidget(2, 2, mycom)

        item_widget = QPushButton("test")
        self.table.setCellWidget(1, 3, item_widget)

        self.table.cellClicked.connect(self.__mycell_clicked)
        mycom.currentTextChanged.connect(self.__mycom_text_changed)

    @pyqtSlot(int, int)
    def __mycell_clicked(self, row, col):
        cell = self.table.item(row, col)
        # print(cell)

        if cell is not None:
            txt = "clicked cell = ({0},{1}) ==>{2}<==".format(row, col, cell.text())
        else:
            txt = "clicked cell = ({0},{1}) ==>None type<==".format(row, col)

        # print(txt)
        self._mainwin.statusbar.showMessage(txt)
        return

    @pyqtSlot(str)
    def __mycom_text_changed(self, txt):
        msg = QMessageBox.information(self, 'combobox changed...', txt)
        return

    def __make_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)

        grid = QGridLayout()
        vbox.addLayout(grid)

        btn1 = QPushButton("delete all")
        grid.addWidget(btn1, 0, 0)
        btn2 = QPushButton("delete table")
        grid.addWidget(btn2, 0, 1)
        btn3 = QPushButton("selection mode")
        grid.addWidget(btn3, 0, 2)
        btn4 = QPushButton("add column")
        grid.addWidget(btn4, 0, 3)

        btn5 = QPushButton("insert column")
        grid.addWidget(btn5, 1, 0)
        btn6 = QPushButton("delete column")
        grid.addWidget(btn6, 1, 1)
        btn7 = QPushButton("add row")
        grid.addWidget(btn7, 1, 2)
        btn8 = QPushButton("insert row")
        grid.addWidget(btn8, 1, 3)

        btn9 = QPushButton("delete row")
        grid.addWidget(btn9, 2, 0)
        btn10 = QPushButton("row unit selection")
        grid.addWidget(btn10, 2, 1)
        btn11 = QPushButton("hide grid line")
        grid.addWidget(btn11, 2, 2)
        btn12 = QPushButton("alternate color")
        grid.addWidget(btn12, 2, 3)

        btn13 = QPushButton("select random row")
        grid.addWidget(btn13, 3, 0)
        btn14 = QPushButton("edit")
        grid.addWidget(btn14, 3, 1)
        btn15 = QPushButton("hide row header")
        grid.addWidget(btn15, 3, 2)
        btn16 = QPushButton("hide column header")
        grid.addWidget(btn16, 3, 3)

        btn17 = QPushButton("selected cells")
        grid.addWidget(btn17, 4, 0)
        btn18 = QPushButton("selected ranges")
        grid.addWidget(btn18, 4, 1)
        btn19 = QPushButton("current cell content")
        grid.addWidget(btn19, 4, 2)
        btn20 = QPushButton("(0,0) cell content")
        grid.addWidget(btn20, 4, 3)

        btn21 = QPushButton("span")
        grid.addWidget(btn21, 5, 0)
        btn22 = QPushButton("change background")
        grid.addWidget(btn22, 5, 1)
        btn23 = QPushButton("change cell background")
        grid.addWidget(btn23, 5, 2)
        btn24 = QPushButton("change color if selected")
        grid.addWidget(btn24, 5, 3)

        btn25 = QPushButton("change header background")
        grid.addWidget(btn25, 6, 0)
        btn26 = QPushButton("(1,2) checkbox value")
        grid.addWidget(btn26, 6, 1)
        btn27 = QPushButton("collation setting")
        grid.addWidget(btn27, 6, 2)
        btn28 = QPushButton("hide column, row")
        grid.addWidget(btn28, 6, 3)

        self.setLayout(vbox)

        self.setGeometry(200, 200, 400, 500)
        self.setWindowTitle("tablewidget example")

        btn1.clicked.connect(self.__btn1_clicked)
        btn2.clicked.connect(self.__btn2_clicked)
        btn3.clicked.connect(self.__btn3_clicked)
        btn4.clicked.connect(self.__btn4_clicked)
        btn5.clicked.connect(self.__btn5_clicked)
        btn6.clicked.connect(self.__btn6_clicked)
        btn7.clicked.connect(self.__btn7_clicked)
        btn8.clicked.connect(self.__btn8_clicked)
        btn9.clicked.connect(self.__btn9_clicked)
        btn10.clicked.connect(self.__btn10_clicked)
        btn11.clicked.connect(self.__btn11_clicked)
        btn12.clicked.connect(self.__btn12_clicked)
        btn13.clicked.connect(self.__btn13_clicked)
        btn14.clicked.connect(self.__btn14_clicked)
        btn15.clicked.connect(self.__btn15_clicked)
        btn16.clicked.connect(self.__btn16_clicked)
        btn17.clicked.connect(self.__btn17_clicked)
        btn18.clicked.connect(self.__btn18_clicked)
        btn19.clicked.connect(self.__btn19_clicked)
        btn20.clicked.connect(self.__btn20_clicked)
        btn21.clicked.connect(self.__btn21_clicked)
        btn22.clicked.connect(self.__btn22_clicked)
        btn23.clicked.connect(self.__btn23_clicked)
        btn24.clicked.connect(self.__btn24_clicked)
        btn25.clicked.connect(self.__btn25_clicked)
        btn26.clicked.connect(self.__btn26_clicked)
        btn27.clicked.connect(self.__btn27_clicked)
        btn28.clicked.connect(self.__btn28_clicked)

    @pyqtSlot()
    def __btn1_clicked(self):
        self.table.clearContents()

    @pyqtSlot()
    def __btn2_clicked(self):
        self.table.clear()

    @pyqtSlot()
    def __btn3_clicked(self):
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    @pyqtSlot()
    def __btn4_clicked(self):
        col_count = self.table.columnCount()
        self.table.setColumnCount(col_count+1)

    @pyqtSlot()
    def __btn5_clicked(self):
        self.table.insertColumn(1)

    @pyqtSlot()
    def __btn6_clicked(self):
        self.table.removeColumn(2)

    @pyqtSlot()
    def __btn7_clicked(self):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count+1)

    @pyqtSlot()
    def __btn8_clicked(self):
        self.table.insertRow(0)

    @pyqtSlot()
    def __btn9_clicked(self):
        self.table.removeRow(1)

    @pyqtSlot()
    def __btn10_clicked(self):
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        return

    @pyqtSlot()
    def __btn11_clicked(self):
        sender_obj = self.sender()
        if sender_obj.text() == "hide grid line":
            self.table.setShowGrid(False)  # hide grid line
            sender_obj.setText("show grid line")
        else:
            self.table.setShowGrid(True)  # hide grid line
            sender_obj.setText("hide grid line")
        return

    @pyqtSlot()
    def __btn12_clicked(self):
        sender_obj = self.sender()
        if sender_obj.text() == "alternate color":
            self.table.setAlternatingRowColors(True)
            sender_obj.setText("no alternate")
        else:
            self.table.setAlternatingRowColors(False)
            sender_obj.setText("alternate color")
        return

    @pyqtSlot()
    def __btn13_clicked(self):
        row_cnt = self.table.rowCount()
        row_idx = random.randint(0, row_cnt-1)

        self.table.selectRow(row_idx)
        return

    @pyqtSlot()
    def __btn14_clicked(self):
        sender_obj = self.sender()
        if sender_obj.text() == "edit":
            self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
            sender_obj.setText("no edit")
        else:
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            sender_obj.setText("edit")
        return

    @pyqtSlot()
    def __btn15_clicked(self):
        sender_obj = self.sender()
        if sender_obj.text() == "hide row header":
            self.table.verticalHeader().setVisible(False)
            sender_obj.setText("show row header")
        else:
            self.table.verticalHeader().setVisible(True)
            sender_obj.setText("hide row header")
        return

    @pyqtSlot()
    def __btn16_clicked(self):
        sender_obj = self.sender()
        if sender_obj.text() == "hide column header":
            self.table.horizontalHeader().setVisible(False)
            sender_obj.setText("show column header")
        else:
            self.table.horizontalHeader().setVisible(True)
            sender_obj.setText("hide column header")
        return

    @pyqtSlot()
    def __btn17_clicked(self):
        aa = self.table.selectedIndexes()
        cell = set( (idx.row(), idx.column()) for idx in aa )

        txt1 = "selected cells ; {0}".format(cell)
        msg = QMessageBox.information(self, 'selectedIndexes()...',  txt1)
        return

    @pyqtSlot()
    def __btn18_clicked(self):
        aa = self.table.selectedRanges()
        txt = []
        for idx, sel in enumerate(aa):

            tmp = "ranage {0} ; row/col Count={1}/{2} ".format(idx,sel.rowCount(), sel.columnCount() ) + \
                  "({0},{1}) ~ ({2},{3})".format(sel.topRow(), sel.leftColumn(), sel.bottomRow(), sel.rightColumn())
            txt.append(tmp)
        msg = QMessageBox.information(self, 'selectedRanges()...', '\n'.join(txt))
        return

    @pyqtSlot()
    def __btn19_clicked(self):
        aa = self.table.currentItem()
        # print(aa)

        if aa is not None:
            txt = "row={0}, column={1}, content={2}".format(aa.row(), aa.column(), aa.text())
        else:
            txt = "clicked cell = ({0},{1}) ==>None type<==".format(self.table.currentRow(), self.table.currentColumn())

        msg = QMessageBox.information(self, 'cell content', txt)
        return

    @pyqtSlot()
    def __btn20_clicked(self):
        item = self.table.item(0, 0)
        if item is not None:
            txt = item.text()
        else:
            txt = "no data"
        msg = QMessageBox.information(self, "(0,0) content", txt)
        return

    @pyqtSlot()
    def __btn21_clicked(self):
        col_count = self.table.columnCount()
        self.table.setColumnCount(col_count+1)
        self.table.setSpan(1, col_count, 2, 1)

        self.table.setCellWidget(1, col_count, QPushButton("span"))

        return

    @pyqtSlot()
    def __btn22_clicked(self):
        """
        random background everytime the button is clicked..

        ** QPalette.Base  ==> use as background of text widget
        :return:
        """
        palette = QPalette()

        x = random.randint(1, 4)
        if x == 1:
            palette.setColor(QPalette.Base, QColor(255, 125, 0))
        elif x == 2:
            palette.setColor(QPalette.Base, Qt.yellow)
        elif x == 3:
            palette.setColor(QPalette.Base, QColor(255, 255, 255))   # white
        else:
            palette.setColor(QPalette.Base, QColor(0, 255, 0))

        self.table.setPalette(palette)
        return

    @pyqtSlot()
    def __btn23_clicked(self):
        x = random.randint(1, 3)
        myitem = self.table.item(0, 0)
        if x == 1:
            myitem.setBackground(QBrush(QColor(0, 0, 255)))
            myitem.setForeground(QBrush(Qt.red))
            myitem.setFont(QFont("Times", 17, QFont.Bold, italic=True))
        elif x == 2:
            myitem.setBackground(QBrush(Qt.red))
            myitem.setForeground(QBrush(Qt.yellow))
            myitem.setFont(QFont("Helvetica", 8, QFont.Normal, italic=False))
        else:
            myitem.setBackground(QBrush(QColor(0, 255, 0)))
            myitem.setForeground(QBrush(Qt.blue))
            myitem.setFont(QFont('SansSerif', 25))
        return

    @pyqtSlot()
    def __btn24_clicked(self):
        """
        ** QPalette.Highlight  ==> set background when item chosen
                                    default ; Qt.darkBlue

        ** QPalette.HighlightedText  ==> set text color when item chosen
                                          default ; Qt.white
        :return:
        """
        palette = QPalette()
        palette.setColor(QPalette.Highlight, Qt.yellow)
        palette.setColor(QPalette.HighlightedText, Qt.red)
        self.table.setPalette(palette)
        return

    @pyqtSlot()
    def __btn25_clicked(self):
        """
        ** set background color of header --> operates when app.setStyle()

        :return:
        """
        hitem = self.table.horizontalHeaderItem(1)
        if hitem is not None:
            hitem.setBackground(QBrush(Qt.cyan))
        return

    @pyqtSlot()
    def __btn26_clicked(self):
        ckbox = self.table.cellWidget(1, 2)
        # print(ckbox)
        if isinstance(ckbox, QCheckBox):
            if ckbox.isChecked():
                print("checked")
                _ = QMessageBox.information(self, 'checkbox', "checked")
            else:
                _ = QMessageBox.information(self, 'checkbox', "no checked")
        else:
            _ = QMessageBox.information(self, 'checkbox', "not a checkbox.")
        return

    @pyqtSlot()
    def __btn27_clicked(self):
        """
        collation possible if header selected
        :return:
        """
        sender_obj = self.sender()
        if sender_obj.text() == "collation setting":
            self.table.setSortingEnabled(True)  # default ; False
            sender_obj.setText("no collation setting")
        else:
            self.table.setSortingEnabled(False)
            sender_obj.setText("collation setting")
        return

    @pyqtSlot()
    def __btn28_clicked(self):
        """
        hide column, row
        :return:
        """
        sender_obj = self.sender()
        if sender_obj.text() == "hide column, row":
            self.table.setColumnHidden(2, True)
            self.table.setRowHidden(0, True)
            sender_obj.setText("show column, row")
        else:
            self.table.setColumnHidden(2, False)
            self.table.setRowHidden(0, False)
            sender_obj.setText("hide column, row")
        return


class MyMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        table = MyTable(self)
        # table.setStyle(QStyleFactory.create('Fusion'))
        self.setCentralWidget(table)

        self.statusbar = self.statusBar()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    w = MyMain()
    w.show()
    sys.exit(app.exec())
