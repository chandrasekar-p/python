import psutil
import time
import requests
import socket
import asyncio

# Set the threshold for disk usage (in percentage)
disk_threshold = 80

# Set the Slack webhook URL and channel details
webhook_url = ''

async def send_notification_async(hostname, disk_percent):
    message = f'The disk on host ---[ {hostname} ]--- is {disk_percent}% full! Please free up some space.'
    payload = {'text': message}

    response = await loop.run_in_executor(None, lambda: requests.post(webhook_url, json=payload))
    if response.status_code != 200:
        print(f'Failed to send Slack notification. Status code: {response.status_code}')

async def check_disk_usage_async(hostname):
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    if disk_percent >= disk_threshold:
        await send_notification_async(hostname, disk_percent)

# Get the hostname
hostname = socket.gethostname()

async def main():
    while True:
        await check_disk_usage_async(hostname)
        await asyncio.sleep(300)  # Sleep for 20 minutes (20 mins * 60 secs)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
