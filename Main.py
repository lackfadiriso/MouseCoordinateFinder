import webbrowser
import pyautogui
import os
key = True
while key == True:
    try:
        fare_x, fare_y = pyautogui.position()
        print(f"Mouse Konum = X:{fare_x}, Y:{fare_y} \n --Bitirmek için (CTRL + C) Giriniz--")
        pyautogui.sleep(2)
        os.system("cls")
    except KeyboardInterrupt:
        print("İşlem Bitirilmiştir iyi günler 😊👍")
        break