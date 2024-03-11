import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Import the main window from the gui module
from gui.main_window import MainWindow

class StreamDeckApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title and initial size of the main window
        self.setWindowTitle('Stream Deck Manager')
        self.setGeometry(300, 300, 800, 600)

        # Initialize and set the main window
        self.mainWindow = MainWindow()
        self.setCentralWidget(self.mainWindow)

        # You can add more initialization settings here

def main():
    app = QApplication(sys.argv)
    mainWindow = StreamDeckApp()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
