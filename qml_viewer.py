import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStatusBar
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtGui import QKeySequence

class QmlViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QML Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.load_button = QPushButton("Load QML File")
        self.load_button.clicked.connect(self.load_qml_file)
        self.layout.addWidget(self.load_button)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.reload_qml)
        self.reload_button.setEnabled(False)
        self.layout.addWidget(self.reload_button)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_qml)
        self.clear_button.setEnabled(False)
        self.layout.addWidget(self.clear_button)

        self.load_button.setShortcut(QKeySequence.Open)
        self.reload_button.setShortcut(QKeySequence("F5"))

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
                self.statusBar.showMessage(f"Error: Failed to load {self.current_qml_file}", 5000)
            else:
                self.statusBar.showMessage(f"Successfully loaded {self.current_qml_file}", 5000)
                self.reload_button.setEnabled(True)
                self.clear_button.setEnabled(True)

    def reload_qml(self):
        self.load_qml()

    def clear_qml(self):
        self.engine.clearComponentCache()
        self.engine.loadData(b"")  # Load an empty QML
        self.current_qml_file = None
        self.reload_button.setEnabled(False)
        self.clear_button.setEnabled(False)
        self.statusBar.showMessage("QML view cleared", 5000)

def main():
    app = QApplication(sys.argv)
    viewer = QmlViewer()
    viewer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
