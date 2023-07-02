import pyautogui 
import time
time.sleep(2)
msg=input("Enter the message:")
number=(int(input("Enter the number:")))
for i in range(number):
    pyautogui.typewrite(msg)
    pyautogui.press('Enter')
 





