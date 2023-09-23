from SpaceInvaderUi import MyGui
from PyQt5.QtWidgets import QApplication



def main():
    app = QApplication([])
    gui = MyGui()
    app.exec_()


if __name__ == ("__main__"):
    main()

