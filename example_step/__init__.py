from ui.ui import * # ui 폴더에 있는 ui.py에서 Ui_class를 불러오겠다.


class Main():
    def __init__(self):
        print("실행할 메인 클래스")

        Ui_class()


if __name__ == "__main__":
    Main()
