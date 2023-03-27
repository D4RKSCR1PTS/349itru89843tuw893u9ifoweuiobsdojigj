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
        if pyautogui.locateCenterOnScreen('Images/BloxFlipComplete.png', confidence = 0.9):
          break
      while True:
        if not pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
          break
      cprint('Joined Rain!', "green")
    if not pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
      pyautogui.hotkey('ctrl','r')
      time.sleep(10)
  except:
    time.sleep(5)