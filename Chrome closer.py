import os
import time
IsRunning = True

print ("Timer Started")

time.sleep(3300)
browserExe = "chrome.exe"
os.system("taskkill /f /im "+browserExe)
