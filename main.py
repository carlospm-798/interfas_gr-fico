"""
Carlos Paredes Márquez.
Crear interfraz gráfica. xd
11/10/2020.
"""
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

# Aplicación de Qt
app = QApplication()
# Crear ventana
window = MainWindow()
# Mostrar ventana
window.show()
# Bucle para ventana
sys.exit(app.exec_())