from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,600)
        self.setWindowTitle("CirruScope by Ross")
        self.setupMenu()

    def setupMenu(self):

        self.menu_bar = self.menuBar()
        
        self.options_menu = self.menu_bar.addMenu("Options")

        self.about_section = self.options_menu.addAction("About")
        self.about_section.triggered.connect(self.show_about_window)

        self.exit_button = self.options_menu.addAction("Exit")
        self.exit_button.triggered.connect(lambda: self.close())

    def show_about_window(self):
        self.msg_box = QMessageBox(self)
        self.msg_box.setIcon(QMessageBox.Icon.Information)
        self.msg_box.setWindowTitle("About")
        self.msg_box.setText("CirruScope\n"
        "By Ross\n"
        "A weather app.")
        self.msg_box.setStyleSheet("")
        self.msg_box.exec()


    def setupUI(self):
        self.main_layout = QGridLayout()
        self.default_img = QPixMap
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()





