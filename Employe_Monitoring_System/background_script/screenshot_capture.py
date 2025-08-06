import os
import time
import random
import datetime
import getpass
import pyautogui
import requests
import smtplib
import win32gui
import ctypes
from PIL import Image, ImageDraw, ImageFont
from email.message import EmailMessage


# ---------------------- CONFIGURATION ----------------------

ADMIN_EMAIL = "tirthbelsare6@gmail.com"
SENDER_EMAIL = "tirthbelsare6@gmail.com"
GMAIL_APP_PASSWORD = "solk uwzo umpp wkoa"  # NOTE: Replace with secure env var in production

HIDDEN_FOLDER_NAME = "SystemActivityLogs"
FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf"
WATERMARK_FONT_SIZE = 20
STOP_FILE = "stop.txt"
DJANGO_UPLOAD_URL = "http://127.0.0.1:8000/upload/"

# ---------------------- EMAIL ALERT (Optional) ----------------------

def send_alert_email(subject, body):
    """
    Sends alert email to admin (disabled by default).
    """
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ADMIN_EMAIL
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)

        print("Alert email sent.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

# ---------------------- ENVIRONMENT SETUP ----------------------

def setup_environment():
    """
    Sets up hidden folders and watermark font.
    Returns: (username, user_screenshot_folder, font_object)
    """
    user = getpass.getuser()
    app_data = os.getenv("APPDATA")

    base_folder = os.path.join(app_data, HIDDEN_FOLDER_NAME)
    user_folder = os.path.join(base_folder, user)

    # Create hidden base folder
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
        os.system(f'attrib +h "{base_folder}"')

    # Create hidden user folder
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
        os.system(f'attrib +h "{user_folder}"')

    font = ImageFont.truetype(FONT_PATH, WATERMARK_FONT_SIZE)
    return user, user_folder, font

# ---------------------- SCREEN LOCK CHECK ----------------------

def is_screen_locked():
   # Check if the user is logged in
    user32 = ctypes.windll.User32
    # Get the current foreground window
    foreground_window = user32.GetForegroundWindow()
    
    # If the foreground window is None, the screen is likely locked
    if foreground_window == 0:
        return True
    
    # Check if the desktop is the foreground window
    desktop_window = win32gui.GetDesktopWindow()
    return foreground_window == desktop_window

# ---------------------- SCREENSHOT HANDLING ----------------------

def capture_and_save_screenshot(user, folder_path, font):
    """
    Takes screenshot, adds watermark, saves it, and uploads it.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    image = pyautogui.screenshot()

    draw = ImageDraw.Draw(image)
    watermark = f"{user} | {timestamp}"
    draw.text((10, 10), watermark, font=font, fill="red")

    filename = f"{user}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    full_path = os.path.join(folder_path, filename)
    image.save(full_path)

    print(f"Saved screenshot at: {full_path}")
    upload_screenshot_to_django(full_path, user, timestamp)

def upload_screenshot_to_django(image_path, username, timestamp):
    """
    Uploads screenshot file to Django backend via API.
    """
    try:
        with open(image_path, 'rb') as img:
            files = {'image': img}
            data = {'username': username, 'timestamp': timestamp}
            response = requests.post(DJANGO_UPLOAD_URL, data=data, files=files)

            if response.status_code == 200:
                print("✅ Screenshot uploaded.")
            else:
                print(f"❌ Upload failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error uploading screenshot: {e}")

# ---------------------- CLEANUP & ALERTS ----------------------

def delete_old_screenshots(folder_path, days_old=7):
    """
    Deletes PNG screenshots older than X days from user's folder.
    """
    now = time.time()
    cutoff = now - (days_old * 86400)
    deleted = 0

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if file.endswith(".png") and os.path.isfile(path):
            if os.path.getctime(path) < cutoff:
                os.remove(path)
                deleted += 1

    if deleted > 0:
        print(f"🗑️ Deleted {deleted} old screenshot(s)")

def handle_manual_stop(user):
    send_alert_email(
        "Script Manually Stopped",
        f"User: {user}\nTime: {datetime.datetime.now()}"
    )

def handle_interruption(user, error_msg):
    send_alert_email(
        "ALERT: Script Interrupted",
        f"User: {user}\nTime: {datetime.datetime.now()}\nError: {error_msg}"
    )

# ---------------------- MAIN LOOP ----------------------

def main():
    user, folder, font = setup_environment()
    print("Screenshot monitoring started.")
    print(datetime.datetime.now().isoformat())

    while True:
        try:
            if os.path.exists(STOP_FILE):
                print("Stop file detected. Exiting...")
                break

            if is_screen_locked():
                print("Screen is locked. Skipping screenshot.")
            else:
                print("Screen active. Capturing screenshot...")
                #capture_and_save_screenshot(user, folder, font)

            delete_old_screenshots(folder)

            wait_time = random.randint(5, 10)
            print(f"Waiting {wait_time} seconds...\n")
            time.sleep(wait_time)

        except KeyboardInterrupt:
            #handle_manual_stop(user)
            break

        except Exception as e:
            handle_interruption(user, str(e))
            break

if __name__ == "__main__":
    main()
