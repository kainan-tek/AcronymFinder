

import os
import sys
import time
from log import Log
import global_var as gl
import resrc.resource as res
from parse_file import Parse_Json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QCompleter
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Signal, QThread, Qt
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, log):
        super(MainWindow, self).__init__()
        self.log = log
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_var()
        self.gui_setup()

    def init_var(self):
        self.input_text_bk = ""
        self.json_dict = {}
        self.dialog = QFileDialog()
        self.msgbox = QMessageBox()
        gl.GuiInfo["cwd"] = os.getcwd()
        gl.GuiInfo["json_file"] = os.path.normpath(os.path.join(gl.GuiInfo["cwd"], gl.GuiInfo["json_file"]))

        json_ops = Parse_Json(gl.GuiInfo["json_file"])
        ret = json_ops.file_read()
        if not ret[0].value == 0:
            msgtext = f'Error type: {ret[0].name}'
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False
        self.json_dict = ret[1]

    def gui_setup(self):
        self.setWindowTitle(f'{gl.GuiInfo["proj"]} {gl.GuiInfo["version"]}')
        adtm_icon = QIcon(QPixmap(":/icon/acronym_icon"))
        self.setWindowIcon(adtm_icon)
        self.ui.guideTextEdit.setStyleSheet(u"background-color: rgb(231, 234, 237);")
        self.ui.textEdit.setStyleSheet(u"background-color: rgb(231, 234, 237);")

        self.ui.actionLoad_File.triggered.connect(self.action_load_file)
        self.ui.actionOpen_File.triggered.connect(self.action_open_file)
        self.ui.actionExit.triggered.connect(self.action_exit)
        self.ui.actionOpen_Log.triggered.connect(self.action_open_log)
        self.ui.actionAbout.triggered.connect(self.action_about)
        self.ui.addButton.clicked.connect(self.call_add_bt)

        self.ui.guideTextEdit.setReadOnly(False)
        self.ui.guideTextEdit.setText(gl.GuideTips)
        self.ui.guideTextEdit.setReadOnly(True)

        self.set_autocomplete()
        self.workthread = WorkThread()
        self.workthread.sinout.connect(self.update_acronym_contents)
        self.workthread.start()

    def update_acronym_contents(self):
        input_text = self.ui.comboBox.currentText().strip()
        if input_text and input_text != self.input_text_bk and self.json_dict:
            self.input_text_bk = input_text
            tmp_flag = False
            for item in self.json_dict:
                if input_text.upper() == item.upper():
                    self.ui.comboBox.insertItem(0, item)
                    self.ui.comboBox.setCurrentIndex(0)
                    self.ui.textEdit.setText(self.json_dict[item])
                    tmp_flag = True
                    break
            if not tmp_flag:
                self.ui.textEdit.setText("")

    def set_autocomplete(self):
        self.completer = QCompleter(self.json_dict.keys())
        self.completer.setFilterMode(Qt.MatchStartsWith)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.comboBox.setCompleter(self.completer)

    def call_add_bt(self):
        combobox_str = self.ui.comboBox.currentText().strip()
        tips_str = self.ui.textEdit.toPlainText().strip()
        if not combobox_str or not tips_str:
            msgtext = 'No acronym or contents for adding'
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False

        json_ops = Parse_Json(gl.GuiInfo["json_file"])
        ret = json_ops.file_read()
        if not ret[0].value == 0:
            msgtext = f'Error type: {ret[0].name}'
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False
        tmp_json_dict = ret[1]

        tmp_flag = False
        for item in tmp_json_dict:
            if combobox_str.upper() == item.upper() and not tips_str == tmp_json_dict[item]:
                tmp_flag = True
                break
        if tmp_flag:
            rst = self.msgbox.question(self, "", "This acronym is already in json,\n\ndo you want to update?")
            if rst:
                tmp_json_dict[item] = tips_str
            else:
                return False
        else:
            rst = self.msgbox.question(self, "", "\nDo you want to add this new acronym?\n")
            if rst:
                tmp_json_dict[combobox_str] = tips_str
            else:
                return False

        ret = json_ops.file_write(tmp_json_dict)
        if not ret.value == 0:
            msgtext = f'Error type: {ret.name}'
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False
        self.json_dict = tmp_json_dict

    def action_load_file(self):
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setNameFilter("Json File(*.json)")
        self.dialog.setViewMode(QFileDialog.Detail)
        if not self.dialog.exec():
            return False
        json_file = self.dialog.selectedFiles()[0]
        if not json_file:
            self.log.info("No json file be selected")
            return False
        self.log.info(f"Json file: {json_file}")

        json_ops = Parse_Json(json_file)
        ret = json_ops.file_read()
        if not ret[0].value == 0:
            msgtext = f'Error type: {ret[0].name}'
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False
        self.json_dict = ret[1]
        self.set_autocomplete()
        gl.GuiInfo["json_file"] = json_file
        self.ui.comboBox.clear()
        self.ui.textEdit.clear()

    def action_open_file(self):
        self.log.info("Starting to open json file.")
        if "nt" in os.name:
            os.startfile(gl.GuiInfo["json_file"])
        else:
            os.system(f'xdg-open {gl.GuiInfo["json_file"]}')

    def action_exit(self):
        sys.exit()

    def action_open_log(self):
        if "nt" in os.name:
            dbg_dirname = os.path.normpath(os.path.join(gl.GuiInfo["win_tmp"], gl.GuiInfo["dbg_reldir"]))
            # subprocess.Popen(f'explorer.exe {dbg_dirname}', close_fds=True)
            os.startfile(dbg_dirname)
        else:
            dbg_dirname = os.path.join(os.path.expanduser('~'), gl.GuiInfo["dbg_reldir"])
            # subprocess.Popen(f'xdg-open {dbg_dirname}', close_fds=True)
            os.system(f'xdg-open {dbg_dirname}')

    def action_about(self):
        self.msgbox.information(self, "About", gl.AboutInfo)

    def closeEvent(self, event):
        if self.workthread.isRunning():
            self.workthread.run_flag = False
            self.workthread.quit()


class WorkThread(QThread):
    sinout = Signal()

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.run_flag = True

    def run(self):
        while self.run_flag:
            self.sinout.emit()
            self.sleep(0.03)


if __name__ == "__main__":
    log = Log()
    app = QApplication(sys.argv)
    window = MainWindow(log)
    window.show()
    sys.exit(app.exec())
