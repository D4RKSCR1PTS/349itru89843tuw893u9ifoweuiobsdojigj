import subprocess, time, os, sys
subprocess.check_call(
  [
    sys.executable, 
    '-m', 
    'pip', 
    'install', 
    'pyautogui', 
    'opencv-python', 
    'termcolor'
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
    if pyautogui.locateCenterOnScreen('Images/RBLXWild.png', confidence = 0.9):
      time.sleep(2)
      pyautogui.moveTo(pyautogui.locateCenterOnScreen('Images/RBLXWild.png', confidence = 0.9))
      time.sleep(0.5)
      pyautogui.click()
      time.sleep(2)
      pyautogui.moveTo(700, 700, 5)
      cprint(f"Successfully joined rain!","green")
      cprint(f"Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","yellow")
      f= open("Logs/RainLogs(RBLXWild).txt","a+")
      f.write(f"Successfully joined rain!\nTimestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n")
      f.close()
      wager = 0
      time.sleep(180)
    if not pyautogui.locateCenterOnScreen('Images/RBLXWild.png', confidence = 0.9):
      wager += 1 
      time.sleep(1)
      if wager == 60:
        wager = 0
        pyautogui.hotkey('ctrl','r') 
  except Exception:
    time.sleep(1)