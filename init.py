import sys
from PyQt5.QtWidgets import QMainWindow,QDesktopWidget, QApplication, QWidget, QTabWidget,QVBoxLayout
from Pages.main import MainTab
from Pages.search import SearchTab
from Pages.settings import SettingsTab
from Pages.login import LoginForm



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'SRS - Demo'
        self.left = 0
        self.top = 0
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MainTabsLayout(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MainTabsLayout(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
        QTabBar::tab 
        { 
            background-color : grey;
            padding: 10px; 
            margin:1px;
            border-radius:5px;
        }
        QTabBar::tab:selected 
        { 
            background-color : black;
            color:white;
        }
        QTabWidget::pane {
            border: 0 solid white;
            margin: 0 -15px -15px -15px;
        }
        """)
        self.tab1 = MainTab(self)
        self.tab2 = SearchTab(self)
        self.tab3 = SettingsTab(self, self.tab1)
        # self.login = LoginForm(self)
        self.tab1.setTab(self.tab3)
        self.tabs.resize(400,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Main")
        self.tabs.addTab(self.tab2,"Search")
        self.tabs.addTab(self.tab3,"Settings")
        
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        # self.tab1.setLayout(self.grid)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    screenShape = QDesktopWidget().screenGeometry()
    ex.resize(screenShape.width(), screenShape.height())
    sys.exit(app.exec_())
#  c:\users\dell\appdata\local\programs\python\python37\python.exe init.py
#("./assets/haarcascade_russian_plate_number.xml","."),("./assets/cars.jpeg","./assets")