import datetime
import os
import requests

# Configuration
END_DATE = datetime.datetime(2026, 5, 29)
START_DATE = datetime.datetime(2025, 12, 1)

def send_telegram_message(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response.text}")

def run_countdown():
    now = datetime.datetime.now()
    total_days = (END_DATE - START_DATE).days
    days_passed = (now - START_DATE).days
    days_left = (END_DATE - now).days
    
    percent = (days_passed / total_days) * 100
    if percent > 100: percent = 100
    
    # Progress bar for the message
    bar = f"[{'█' * int(percent / 5)}{'░' * (20 - int(percent / 5))}] {percent:.2f}%"
    
    # Send Telegram Notification
    notification = (
        f"📢 *Industrial Training Update*\n\n"
        f"{bar}\n\n"
        f"Only *{days_left} days* left until May 29, 2026! 🚀"
    )
    send_telegram_message(notification)

if __name__ == "__main__":
    run_countdown()
