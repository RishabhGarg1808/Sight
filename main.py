import sys
from PySide6.QtWidgets import QApplication
from ui.src.init import LoadingSplashScreen
from ui.src.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = LoadingSplashScreen()
    main_window = MainWindow()

    #connecting signals and slots
    splash.model_loaded.connect(main_window.on_modelLoad)
   
    #show the ui after connecting 
    splash.init()
    main_window.show()
    sys.exit(app.exec())