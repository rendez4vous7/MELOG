import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QPlainTextEdit,
    QGraphicsView,
    QGraphicsScene,
    QLabel,
    QSplitter,
    QStatusBar,
    QTreeWidget,
    QTreeWidgetItem,
    QDockWidget,
    QTabWidget,
    QToolBar,
    QPushButton,
    QComboBox,
    QListWidget,
    QFormLayout,
    QSpinBox,
)

from PyQt6.QtGui import (
    QPainter,
    QPen,
    QFont,
    QColor,
    QAction,
)

from PyQt6.QtCore import Qt


class MelogGraphicEngine(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.setStyleSheet("""
            background-color: #1e1e1e;
            border: 1px solid #444;
        """)

        self.draw_grid()
        self.draw_demo()

    def draw_grid(self):

        line_pen = QPen(QColor("#cfcfcf"), 1)

        left = 40
        top = 40
        width = 900
        row_height = 60

        # Horizontal Line
        for i in range(7):
            y = top + i * row_height
            self.scene.addLine(left, y, left + width, y, line_pen)

        # Vertical Line
        for x in range(left, left + width + 1, 60):
            self.scene.addLine(x, top, x, top + 360, line_pen)

        # String Number
        for i in range(6):
            label = self.scene.addText(str(i + 1))
            label.setDefaultTextColor(QColor("white"))
            label.setPos(10, top + i * 60 + 15)

        # Time
        times = ["0:00:00", "0:12:00", "0:29:00", "0:32:30"]

        for i, t in enumerate(times):
            text = self.scene.addText(t)
            text.setDefaultTextColor(QColor("#aaaaaa"))
            text.setPos(50 + i * 180, 5)

    def draw_demo(self):

        notes = [
            (120, 150, "4"),
            (260, 150, "4"),
            (420, 180, "3"),
            (700, 150, "2"),
        ]

        for x, y, value in notes:

            text = self.scene.addText(value)
            text.setDefaultTextColor(QColor("white"))
            text.setFont(QFont("Consolas", 18))
            text.setPos(x, y)

            self.scene.addLine(
                x + 10,
                y + 30,
                x + 10,
                y + 70,
                QPen(QColor("white"), 2)
            )

        error = self.scene.addText("Dissonance!")
        error.setDefaultTextColor(QColor("#ff8080"))
        error.setPos(520, 180)


class MelogIDE(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MELOG IDE")
        self.setGeometry(100, 100, 1600, 900)

        self.setup_ui()
        self.apply_theme()

        self.show_status("Ready")

    def setup_ui(self):

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.create_toolbar()
        self.create_left_sidebar()
        self.create_right_panel()
        self.create_center()
        self.create_bottom_tabs()

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(QAction("New", self))
        toolbar.addAction(QAction("Open", self))
        toolbar.addAction(QAction("Save", self))
        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Domain"))
        self.domain_combo = QComboBox()
        self.domain_combo.addItems([
            "ROBOTICS",
            "AEROSPACE",
            "QUANT",
        ])

        toolbar.addWidget(self.domain_combo)
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Compile"))
        toolbar.addWidget(QPushButton("Run"))

    def create_left_sidebar(self):

        dock = QDockWidget("System Explorer", self)
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        root = QTreeWidgetItem(["ROBOTICS Domain"])
        units = QTreeWidgetItem(["Units"])
        units.addChildren([
            QTreeWidgetItem(["Sequence 1"]),
            QTreeWidgetItem(["Sequence 2"]),
        ])

        root.addChild(units)
        root.addChild(QTreeWidgetItem(["Templates"]))
        root.addChild(QTreeWidgetItem(["Libraries"]))
        root.addChild(QTreeWidgetItem(["Files"]))
        tree.addTopLevelItem(root)
        tree.expandAll()
        dock.setWidget(tree)

        self.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea,
            dock
        )

    def create_right_panel(self):

        dock = QDockWidget("Inspector Panel", self)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(QLabel("Selected Node: K'45"))
        form = QFormLayout()

        string_box = QSpinBox()
        string_box.setValue(1)

        fret_box = QSpinBox()
        fret_box.setValue(2)

        role_combo = QComboBox()
        role_combo.addItems([
            ".Local",
            "Agent ^",
            "Target _",
        ])

        form.addRow("String", string_box)
        form.addRow("Fret", fret_box)
        form.addRow("Role", role_combo)

        layout.addLayout(form)
        layout.addWidget(QLabel("Validation Errors"))

        errors = QListWidget()
        errors.addItem("None")

        layout.addWidget(errors)

        dock.setWidget(container)

        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea,
            dock
        )

    def create_center(self):

        central = QWidget()
        layout = QVBoxLayout(central)
        vertical = QSplitter(Qt.Orientation.Vertical)
        horizontal = QSplitter(Qt.Orientation.Horizontal)

        # Graphical
        graphics_tabs = QTabWidget()

        self.visualizer = MelogGraphicEngine()

        graphics_tabs.addTab(
            self.visualizer,
            "Graphical Mode Score"
        )

        # Linear
        editor_tabs = QTabWidget()

        self.editor = QPlainTextEdit()
        self.editor.setFont(QFont("Consolas", 12))
        self.editor.setPlainText(
            "(ROBOTICS)\n"
            "[#][G>][N'3][T:2^][K'45][M'0][S:7_] ||"
        )
        self.editor.textChanged.connect(
            self.on_text_changed
        )

        self.on_text_changed

        editor_tabs.addTab(
            self.editor,
            "Linear Mode Editor"
        )

        horizontal.addWidget(graphics_tabs)
        horizontal.addWidget(editor_tabs)
        horizontal.setSizes([900, 500])

        self.bottom_tabs = QTabWidget()

        vertical.addWidget(horizontal)
        vertical.addWidget(self.bottom_tabs)
        vertical.setSizes([700, 200])

        layout.addWidget(vertical)

        self.setCentralWidget(central)

    def create_bottom_tabs(self):

        console = QPlainTextEdit()
        console.setReadOnly(True)
        console.setPlainText(
            "Vowel        Meaning\n"
            "N=1 (Time)   a=Neutral\n"
            "T=2 (Joint)  e=Forward\n"
            "K=3 (Value)  o=Repeat\n"
        )

        errors = QPlainTextEdit()
        errors.setReadOnly(True)
        errors.setPlainText(
            "1 Dissonance detected in grid (2, 6)"
        )

        phonology = QPlainTextEdit()
        phonology.setReadOnly(True)

        self.bottom_tabs.addTab(console, "Console")
        self.bottom_tabs.addTab(phonology, "Phonology")
        self.bottom_tabs.addTab(errors, "Errors")

    def apply_theme(self):

        self.setStyleSheet("""

            QMainWindow {
                background-color: #252526;
            }

            QWidget {
                background-color: #252526;
                color: #dddddd;
            }

            QTextEdit,
            QPlainTextEdit,
            QTreeWidget,
            QListWidget {
                background-color: #1e1e1e;
                border: 1px solid #444;
                color: #dddddd;
            }

            QToolBar {
                background-color: #2d2d30;
                border-bottom: 1px solid #444;
            }

            QPushButton {
                background-color: #3c3c3c;
                border: 1px solid #555;
                padding: 4px 8px;
            }

            QPushButton:hover {
                background-color: #505050;
            }

            QDockWidget::title {
                background-color: #333333;
                padding: 4px;
            }

        """)

    def show_status(self, message):
        self.status.showMessage(message)

    def on_text_changed(self):

        text = self.editor.toPlainText()

        if "ROBOTICS" in text:
            self.show_status("ROBOTICS Domain Active")
        else:
            self.show_status("Ready")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MelogIDE()
    window.show()
    sys.exit(app.exec())