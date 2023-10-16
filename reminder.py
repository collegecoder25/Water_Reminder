import pywhatkit as pw
import time
import pyautogui as pg


text = "This is your half hourly reminder to drink water."
hour = 20
minute = 43
while(True):
    pw.sendwhatmsg("+91XXXXXXXXXX",text,hour, minute)
    time.sleep(30)
    pg.press("enter")
    if(minute+3>60):
        hour = (hour+1)%24
    minute = (minute+3) % 60