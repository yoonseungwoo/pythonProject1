    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
    from PyQt5.QtGui import QIcon


    class MyApp(QMainWindow):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            exitAction = QAction('Add model', self)
            exitAction.setShortcut('Ctrl+Q')
            exitAction.setStatusTip('Add application')
            exitAction.triggered.connect(qApp.quit)

            self.statusBar()

            menubar = self.menuBar()
            menubar.setNativeMenuBar(False)
            filemenu = menubar.addMenu('&File')
            filemenu.addAction(exitAction)

            self.setWindowTitle('Etch Test Fixture')
            self.setWindowIcon(QIcon('lam.jpg'))
            self.resize(800, 600)
            self.show()


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())