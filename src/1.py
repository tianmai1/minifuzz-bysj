import sys
import markdown
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QDialog, QPlainTextEdit

class MarkdownDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Markdown Dialog")

        layout = QVBoxLayout()

        self.text_edit = QPlainTextEdit()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def set_markdown_content(self, content):
        html = markdown.markdown(content)
        self.text_edit.setPlainText(html)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        button = QPushButton("Open Markdown Dialog")
        button.clicked.connect(self.show_markdown_dialog)
        layout.addWidget(button)

        self.setLayout(layout)

    def show_markdown_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Markdown File", "", "Markdown Files (*.md)")

        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                markdown_text = file.read()

            dialog = MarkdownDialog(self)
            dialog.set_markdown_content(markdown_text)
            dialog.exec_()

app = QApplication(sys.argv)

widget = MyWidget()
widget.show()

sys.exit(app.exec_())