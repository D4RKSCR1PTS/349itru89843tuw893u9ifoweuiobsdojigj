import subprocess, time, os, sys
subprocess.check_call(
  [
    sys.executable, 
    '-m', 
    'pip', 
    'install', 
    'pyautogui',
    'opencv-python', 
    'termcolor', 
  ]
)
try: 
  os.system('cls')
except:
  os.system('clear')
import pyautogui; from termcolor import cprint
os.system(f'title RBLXRain ^')
cprint('██████╗░░░██╗██╗██████╗░██╗░░██╗░██████╗░█████╗░██████╗░░░███╗░░██████╗░████████╗░██████╗\n██╔══██╗░██╔╝██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗░████║░░██╔══██╗╚══██╔══╝██╔════╝\n██║░░██║██╔╝░██║██████╔╝█████═╝░╚█████╗░██║░░╚═╝██████╔╝██╔██║░░██████╔╝░░░██║░░░╚█████╗░\n██║░░██║███████║██╔══██╗██╔═██╗░░╚═══██╗██║░░██╗██╔══██╗╚═╝██║░░██╔═══╝░░░░██║░░░░╚═══██╗\n██████╔╝╚════██║██║░░██║██║░╚██╗██████╔╝╚█████╔╝██║░░██║███████╗██║░░░░░░░░██║░░░██████╔╝\n╚═════╝░░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░', 'cyan')
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
cprint("AutoRain Enabled! Press Ctrl + C to exit. Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
while True:
  try:
    if pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
      time.sleep(2)
      pyautogui.moveTo(pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9))
      time.sleep(0.5)
      pyautogui.click()
      time.sleep(2)
      pyautogui.moveTo(700, 700, 5)
      while True:
        time.sleep(0.1)
        if pyautogui.locateCenterOnScreen('Images/BloxFlipComplete.png', confidence = 0.9):
          break
      while True:
        time.sleep(0.1)
        if not pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
          break
      f= open("Logs/RainLogs(BloxFlip).txt","a+")
      f.write(f"Successfully joined rain!\nTimestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n")
      f.close()
      cprint(f"\nSuccessfully joined rain!","green")
      cprint("Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
    if not pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
      time.sleep(1)
  except:
    time.sleep(5)