import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PieChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a Figure and a set of subplots
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set the background color of the figure to be transparent
        self.figure.patch.set_alpha(0)

        # Create data for the pie chart
        labels = ["Category A", "Category B", "Category C", "Category D"]
        sizes = [15, 30, 45, 10]
        colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]

        # Plot the pie chart
        self.ax.pie(
            sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140
        )

        # Set aspect ratio to be equal so that the pie is drawn as a circle.
        self.ax.axis("equal")

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        pie_chart_widget = PieChartWidget()
        layout.addWidget(pie_chart_widget)

        central_widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
