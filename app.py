import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QFile
from PyQt5.uic import loadUi
import pyuac
import sys
import attach_commands_to_button
import init_stacked_widget


def my_print():
    print("hello world")


@pyuac.main_requires_admin
def main():
    app = QApplication(sys.argv)
    # Load the UI file
    ui_file_path = "appui.ui"
    ui = loadUi(ui_file_path)
    # Show the main window
    init_stacked_widget.init_stacked_widget(ui)
    attach_commands_to_button.attach(ui)
    # ui.run_MRT_btn.clicked.connect(ui_action.run_mrt.run_mrt)
    # ui.run_taskmanager_btn.clicked.connect(ui_action.run_taskmanger.run_taskmanger)
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
