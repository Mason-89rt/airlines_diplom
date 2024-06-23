from PyQt5 import QtWidgets


class TableDataHandler:
    @staticmethod
    def populate_table(table, data):
        if isinstance(table, QtWidgets.QTableWidget) and isinstance(data, list):
            table.setRowCount(len(data))
            for row, item in enumerate(data):
                for col, key in enumerate(item.keys()):
                    table_item = QtWidgets.QTableWidgetItem(str(item[key]))
                    table.setItem(row, col, table_item)
