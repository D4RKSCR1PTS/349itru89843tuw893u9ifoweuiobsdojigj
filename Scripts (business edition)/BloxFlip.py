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
    'cloudscraper'
  ]
)
try: 
  os.system('cls')
except:
  os.system('clear')
import pyautogui, cloudscraper ; from termcolor import cprint
os.system(f'title RBLXRain ^')
cprint('██████╗░░░██╗██╗██████╗░██╗░░██╗░██████╗░█████╗░██████╗░░░███╗░░██████╗░████████╗░██████╗\n██╔══██╗░██╔╝██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗░████║░░██╔══██╗╚══██╔══╝██╔════╝\n██║░░██║██╔╝░██║██████╔╝█████═╝░╚█████╗░██║░░╚═╝██████╔╝██╔██║░░██████╔╝░░░██║░░░╚█████╗░\n██║░░██║███████║██╔══██╗██╔═██╗░░╚═══██╗██║░░██╗██╔══██╗╚═╝██║░░██╔═══╝░░░░██║░░░░╚═══██╗\n██████╔╝╚════██║██║░░██║██║░╚██╗██████╔╝╚█████╔╝██║░░██║███████╗██║░░░░░░░░██║░░░██████╔╝\n╚═════╝░░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░', 'cyan')
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
cprint("AutoRain Enabled! Press Ctrl + C to exit. Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
while True:
  try:
    r = cloudscraper.create_scraper().get('http://rest-bf.blox.land/chat/history').json()
    check = r['rain']
    if check['active'] == True:
      if pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
        time.sleep(2)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9))
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(700, 700, 5)
        waiting = ((check['duration']/(1000*60))%60*60+10)
        duration = int(check['duration']/(1000*60))%60
        grabprize = str(check['prize'])[:-2]
        prize = (format(int(grabprize),","))
        host = check['host']
        f= open("Logs/RainLogs(BloxFlip).txt","a+")
        f.write(f"Successfully joined rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n")
        f.close()
        cprint(f"\nSuccessfully joined rain!","green")
        cprint(f"Rain amount: {prize} R$", "cyan")
        cprint(f"Expiration: {duration} minutes","red")
        cprint(f"Host: {host}","yellow")
        cprint("Timestamp: " + time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(int(time.time()))) + "\n","magenta")
        time.sleep(waiting)
      if not pyautogui.locateCenterOnScreen('Images/BloxFlip.png', confidence = 0.9):
        pyautogui.hotkey('ctrl','r')
        time.sleep(10)
    elif check['active'] == False:
      time.sleep(5)
  except:
    time.sleep(5)