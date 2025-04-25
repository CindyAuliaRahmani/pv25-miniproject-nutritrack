import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
)
from PyQt5.QtCore import Qt
from nutritrack import Ui_MainWindow 

class NutriTrackApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Nutri Track")

        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Nama", "Kalori", "Kategori", "Sehat", "Kenyang"])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.comboBoxKategori.addItem("")
        self.ui.comboBoxKategori.addItems(["Sarapan", "Makan Siang", "Makan Malam", "Snack"])
        self.ui.comboBoxKategori.setCurrentIndex(0) 
        self.ui.sliderKenyang.setMinimum(0)
        self.ui.sliderKenyang.setMaximum(10)
        self.ui.sliderKenyang.setValue(5)

        self.ui.spinBoxKalori.setMaximum(2000)
        self.ui.spinBoxKalori.setValue(0)

        self.total_kalori = 0
        self.ui.buttonTambah.clicked.connect(self.tambah_makanan)

    def tambah_makanan(self):
        nama = self.ui.lineEditNama.text()
        kalori = self.ui.spinBoxKalori.value()
        kategori = self.ui.comboBoxKategori.currentText()
        sehat = "Ya" if self.ui.checkBoxSehat.isChecked() else "Tidak"
        kenyang = self.ui.sliderKenyang.value()

        if not nama:
            QMessageBox.warning(self, "Peringatan", "Nama makanan tidak boleh kosong.")
            return

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(nama))
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(kalori)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(kategori))
        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(sehat))
        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(kenyang)))

        self.total_kalori += kalori
        self.ui.labelTotalKalori.setText(f"Total Kalori: {self.total_kalori} kkal")
        self.ui.lineEditNama.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NutriTrackApp()
    window.show()
    sys.exit(app.exec_())
