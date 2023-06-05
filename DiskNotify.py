import psutil
import time
import requests
import socket

# Set the threshold for disk usage (in percentage)
disk_threshold = 80

# Set the Slack webhook URL and channel details
webhook_url = ''

def send_notification(hostname, disk_percent):
    message = f'The disk on host ---[ {hostname} ]--- is {disk_percent}% full! Please free up some space.'
    payload = {'text': message}

    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f'Failed to send Slack notification. Status code: {response.status_code}')

def check_disk_usage(hostname):
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    if disk_percent >= disk_threshold:
        send_notification(hostname, disk_percent)
        time.sleep(60)  # Sleep for 20 minutes (20 mins * 60 secs)

# Get the hostname
hostname = socket.gethostname()

# Continuously check disk usage until it's resolved
while True:
    check_disk_usage(hostname)
