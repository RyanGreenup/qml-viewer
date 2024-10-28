import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStatusBar, QHBoxLayout, QFrame, QSizePolicy, QMenuBar, QMenu
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction, QKeySequence

class QmlViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QML Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Create File menu
        self.file_menu = QMenu("&File", self)
        self.menu_bar.addMenu(self.file_menu)

        # Create actions
        self.load_action = QAction("&Load QML File", self)
        self.load_action.setShortcut("Ctrl+O")
        self.load_action.triggered.connect(self.load_qml_file)
        self.file_menu.addAction(self.load_action)

        self.reload_action = QAction("&Reload", self)
        self.reload_action.setShortcut(QKeySequence("F5"))
        self.reload_action.triggered.connect(self.reload_qml)
        self.reload_action.setEnabled(False)
        self.file_menu.addAction(self.reload_action)

        self.clear_action = QAction("&Clear", self)
        self.clear_action.setShortcut(QKeySequence("Ctrl+L"))
        self.clear_action.triggered.connect(self.clear_qml)
        self.clear_action.setEnabled(False)
        self.file_menu.addAction(self.clear_action)

        self.file_menu.addSeparator()

        self.exit_action = QAction("E&xit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create a frame for the buttons
        self.button_frame = QFrame()
        self.button_frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.button_layout = QHBoxLayout(self.button_frame)

        self.load_button = QPushButton("Load QML File")
        self.load_button.clicked.connect(self.load_action.trigger)
        self.button_layout.addWidget(self.load_button)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.reload_action.trigger)
        self.reload_button.setEnabled(False)
        self.button_layout.addWidget(self.reload_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_action.trigger)
        self.clear_button.setEnabled(False)
        self.button_layout.addWidget(self.clear_button)

        # Add stretches to center the buttons
        self.button_layout.insertStretch(0, 1)
        self.button_layout.addStretch(1)

        # Set button layout spacing and margins
        self.button_layout.setSpacing(10)
        self.button_layout.setContentsMargins(10, 10, 10, 10)

        # Add the button frame to the main layout
        self.main_layout.addWidget(self.button_frame)

        # Create a placeholder widget for the QML view
        self.qml_placeholder = QWidget()
        self.qml_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.qml_placeholder)

        # Set main layout spacing and margins
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.setStatusBar(QStatusBar())

        self.engine = QQmlApplicationEngine()
        self.current_qml_file = None

    def load_qml_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open QML File", "", "QML Files (*.qml)")
        if file_name:
            self.current_qml_file = file_name
            self.load_qml()

    def load_qml(self):
        if self.current_qml_file:
            self.engine.clearComponentCache()
            self.engine.load(QUrl.fromLocalFile(self.current_qml_file))
            if not self.engine.rootObjects():
                self.statusBar().showMessage(f"Error: Failed to load {self.current_qml_file}", 5000)
            else:
                self.statusBar().showMessage(f"Successfully loaded {self.current_qml_file}", 5000)
                self.reload_button.setEnabled(True)
                self.clear_button.setEnabled(True)
                self.reload_action.setEnabled(True)
                self.clear_action.setEnabled(True)

    def reload_qml(self):
        self.load_qml()

    def clear_qml(self):
        self.engine.clearComponentCache()
        self.engine.loadData(b"")  # Load an empty QML
        self.current_qml_file = None
        self.reload_button.setEnabled(False)
        self.clear_button.setEnabled(False)
        self.reload_action.setEnabled(False)
        self.clear_action.setEnabled(False)
        self.statusBar().showMessage("QML view cleared", 5000)

def main():
    app = QApplication(sys.argv)
    viewer = QmlViewer()
    viewer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
