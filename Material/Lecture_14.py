
import schedule
import time
import pyautogui
import shutil
import os

# 1. Scheduling Tasks with schedule
def task():
    print("Executing Job...")

schedule.every(5).seconds.do(task)
schedule.every(5).minutes.do(task)
schedule.every(5).hours.do(task)
schedule.every(5).days.do(task)
schedule.every(5).weeks.do(task)
schedule.every().monday.do(task)
schedule.every().wednesday.at("11:45:20").do(task)

# Run the schedule for a limited time
end_time = time.time() + 20
while time.time() < end_time:
    schedule.run_pending()
    time.sleep(1)

# 2. File Backup Task with schedule
def backup(source_folder, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"Backed up: {filename}")
    except Exception as e:
        print(f"Error during backup: {e}")

source_folder = "/path/to/source_folder"
destination_folder = "/path/to/destination_folder"
schedule.every().day.at("18:30").do(backup, source_folder, destination_folder)

# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)

# 3. Basic Mouse Control with pyautogui
screenWidth, screenHeight = pyautogui.size()
print("Screen Width:", screenWidth)
print("Screen Height:", screenHeight)
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.click()
pyautogui.moveTo(100, 100)
pyautogui.dragTo(400, 100, duration=1)

# 4. Keyboard Automation with pyautogui
pyautogui.press('win')
pyautogui.write('Notepad')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("Hello, world!")
pyautogui.hotkey('ctrl', 's')

# 5. Taking Screenshots with pyautogui
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
region_screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))
region_screenshot.save('region_screenshot.png')

# 6. Finding an Image on the Screen with pyautogui
location = pyautogui.locateOnScreen('example.png')
if location:
    print(f"Image found at: {location}")
    pyautogui.moveTo(location.left + location.width / 2, location.top + location.height / 2)
    pyautogui.click(location)
else:
    print("Image not found!")
