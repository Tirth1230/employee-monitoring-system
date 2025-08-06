# import pyautogui
# from PIL import Image, ImageDraw, ImageFont
# import os
# import getpass
# import datetime
# import random
# import time
# import smtplib
# from email.message import EmailMessage


# # ---------------------- CONFIGURATION ----------------------

# ADMIN_EMAIL = "tirthbelsare6@gmail.com"
# SENDER_EMAIL = "tirthbelsare6@gmail.com"
# GMAIL_APP_PASSWORD = "solk uwzo umpp wkoa"
# HIDDEN_FOLDER_NAME = "SystemActivityLogs"
# FONT_PATH = "C:\\Windows\\Fonts\\arial.ttf"
# WATERMARK_FONT_SIZE = 20
# STOP_FILE = "stop.txt"


# # ---------------------- UTILITY FUNCTIONS ----------------------


# def send_alert_email(subject, body):
#     """
#     Sends an alert email using Gmail SMTP.
#     """
#     try:
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = SENDER_EMAIL
#         msg["To"] = ADMIN_EMAIL
#         msg.set_content(body)

#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#             smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
#             smtp.send_message(msg)

#         print("Alert email sent.")

#     except Exception as e:
#         print(f"Failed to send alert email: {e}")


# def delete_old_screenshots(folder_path, days_old=7):
#     """
#     Deletes screenshot files older than X days to save space.
#     """
#     now = time.time()
#     cutoff = now - (days_old * 86400)
#     deleted = 0

#     for file in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file)
#         if os.path.isfile(file_path) and file.endswith(".png"):
#             if os.path.getctime(file_path) < cutoff:
#                 print(os.path.getctime(file_path))
#                 os.remove(file_path)
#                 deleted += 1

#     if deleted > 0:
#         print(f"Deleted {deleted} old screenshot(s).\n")


# def setup_environment():
#     """
#     Sets up user, folder, and watermark font.
#     """
#     user = getpass.getuser()
#     app_data = os.getenv("APPDATA")
#     folder = os.path.join(app_data, HIDDEN_FOLDER_NAME)

#     if not os.path.exists(folder):
#         os.makedirs(folder)
#         os.system(f'attrib +h "{folder}"')

#     font = ImageFont.truetype(FONT_PATH, WATERMARK_FONT_SIZE)

#     return user, folder, font


# def capture_and_save_screenshot(user, folder_path, font):
#     """
#     Takes a screenshot, adds watermark, and saves it.
#     """
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     image = pyautogui.screenshot()
#     draw = ImageDraw.Draw(image)

#     watermark = f"{user} | {timestamp}"
#     draw.text((10, 10), watermark, font=font, fill="red")

#     filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
#     full_path = os.path.join(folder_path, filename)
#     image.save(full_path)

#     print(f"Saved screenshot at: {full_path}")


# def handle_manual_stop(user):
#     subject = "Script Manually Stopped"
#     body = (
#         f"Screenshot monitoring was manually stopped.\n"
#         f"User: {user}\n"
#         f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     )
#     send_alert_email(subject, body)


# def handle_interruption(user, error_msg):
#     subject = "ALERT: Script Interrupted"
#     body = (
#         f"Screenshot monitoring crashed or was interrupted.\n"
#         f"User: {user}\n"
#         f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
#         f"Error: {error_msg}"
#     )
#     send_alert_email(subject, body)


# # ---------------------- MAIN LOOP ----------------------


# def main():
#     user, folder_path, watermark_font = setup_environment()
#     print("Screenshot monitoring started (background mode).")

#     while True:
#         try:
#             if os.path.exists(STOP_FILE):
#                 print("Stop file detected. Exiting...")
#                 break

#             delete_old_screenshots(folder_path)
#             capture_and_save_screenshot(user, folder_path, watermark_font)

#             wait_time = random.randint(60, 300)
#             print(f"Waiting {wait_time} seconds...\n")
#             time.sleep(wait_time)

#         except KeyboardInterrupt:
#             handle_manual_stop(user)
#             break

#         except Exception as e:
#             handle_interruption(user, e)
#             break


# if __name__ == "__main__":
#     main()

import socket
print(socket.gethostname(),socket.gethostbyname(socket.gethostname()))