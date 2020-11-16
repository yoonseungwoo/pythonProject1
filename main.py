
#Make File
import sys
from PyQt5.QtWidgets import *
import os

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Upper Part Number')
        self.qle1 = QLineEdit()

        lbl2 = QLabel('Part Number')
        self.qle2 = QLineEdit()

        lbl3 = QLabel('Description')
        self.qle3 = QLineEdit()

        lbl4 = QLabel('Qty')
        self.qle4 = QLineEdit()

        btn = QPushButton('Save Model')
        btn.clicked.connect(self.makeFile_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.qle1)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.qle2)
        vbox.addWidget(lbl3)
        vbox.addWidget(self.qle3)
        vbox.addWidget(lbl4)
        vbox.addWidget(self.qle4)
        vbox.addWidget(btn)

        self.setLayout(vbox)

        self.setWindowTitle('makeFile')
        self.setGeometry(100, 100, 250, 300)
        self.show()

    def makeFile_btn(self):
        if len(self.qle1.text()) == 0 or len(self.qle2.text()) == 0 or len(self.qle3.text()) == 0 or len(self.qle4.text()) == 0:
            return

        directory = self.qle1.text()
        name = self.qle2.text() + '.txt'
        content = self.qle1.text() + self.qle2.text()
        filename = directory + name
        mkfile = open(filename, 'w')
        mkfile.write(content)
        mkfile.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())