from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMenuBar, QStatusBar, QTabWidget, QAction

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Menu Bar
        self.menuBar = QMenuBar(self)
        fileMenu = self.menuBar.addMenu('File')
        editMenu = self.menuBar.addMenu('Edit')
        helpMenu = self.menuBar.addMenu('Help')

        # Adding actions to the menu bar
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)  # Connects the action to close the window
        fileMenu.addAction(exitAction)

        layout.setMenuBar(self.menuBar)

        # Status Bar
        self.statusBar = QStatusBar(self)
        self.statusBar.showMessage('Ready')
        layout.addWidget(self.statusBar)

        # Tabs
        self.tabWidget = QTabWidget(self)
        self.tabWidget.addTab(QLabel('Button Configuration'), 'Buttons')
        self.tabWidget.addTab(QLabel('Profiles'), 'Profiles')
        self.tabWidget.addTab(QLabel('Plugin Management'), 'Plugins')
        layout.addWidget(self.tabWidget)

        self.setLayout(layout)

        # You can further customize the actions and add more functionality
