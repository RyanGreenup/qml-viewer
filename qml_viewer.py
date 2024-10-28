import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl

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
                print(f"Error: Failed to load {self.current_qml_file}")
            else:
                self.reload_button.setEnabled(True)

    def reload_qml(self):
        self.load_qml()

def main():
    app = QApplication(sys.argv)
    viewer = QmlViewer()
    viewer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
