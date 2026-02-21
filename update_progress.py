import datetime
import os
import requests

# Configuration
END_DATE = datetime.datetime(2026, 5, 29)
START_DATE = datetime.datetime(2026, 1, 14) # Adjust this to your start date

def send_telegram_message(message):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=data)

def update_readme():
    now = datetime.datetime.now()
    total_days = (END_DATE - START_DATE).days
    days_passed = (now - START_DATE).days
    days_left = (END_DATE - now).days
    
    percent = (days_passed / total_days) * 100
    if percent > 100: percent = 100
    
    bar = f"[{'█' * int(percent / 5)}{'░' * (20 - int(percent / 5))}] {percent:.2f}%"
    status_text = f"🚀 **Industrial Training Progress:** {bar} \n\n📅 **{days_left} days** remaining until May 29, 2026!"

    # Update README file
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    import re
    pattern = r".*?"
    replacement = f"\n{status_text}\n"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    # Send Telegram Notification
    notification = f"📢 *LI Progress Update*\n\n{bar}\n\nOnly *{days_left} days* left until you finish your industrial training! Keep it up! 💪"
    send_telegram_message(notification)

if __name__ == "__main__":
    update_readme()
