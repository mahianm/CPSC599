import serial
import pyautogui
import time

ser = serial.Serial('COM4', 9600)  
button_press_count = 0

while True:
    if ser.readable():
        signal = ser.readline().decode().strip()

        if signal == "BUTTON_PRESSED":
            button_press_count += 1

            if button_press_count % 2 == 1:  
                pyautogui.hotkey('space')
                pyautogui.hotkey('ctrl', 't')
                time.sleep(1)
                pyautogui.typewrite("https://www.youtube.com/watch?v=0NKUpo_xKyQ")
                pyautogui.press('enter')
                print("Odd Video opened")
            else:
                # Play the second video
                pyautogui.hotkey('space')
                pyautogui.hotkey('ctrl', 't')
                time.sleep(1)
                pyautogui.typewrite("https://www.youtube.com/watch?v=AAbiC27WB3w")
                pyautogui.press('enter')
                print("Even Video opened")
