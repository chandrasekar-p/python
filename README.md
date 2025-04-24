# Disk Usage Monitor with Slack Notifications

This Python script monitors disk usage on a server and sends an alert to a specified Slack channel if the usage exceeds a defined threshold.

## 📦 Features

- Monitors disk space on the root directory (`/`)
- Sends Slack notifications when disk usage exceeds the threshold
- Runs continuously and checks every 20 minutes
- Asynchronous implementation using `asyncio` for efficiency

## Requirements

- Python 3.7 or higher
- Internet connection
- Slack Incoming Webhook URL

## Installation

1. Clone the repository or copy the script to your server.
2. Install dependencies:

```bash
pip install psutil requests
```

## 🔧 Configuration

Edit the script to set your Slack webhook URL:

```
webhook_url = '<slack webhook url>'
```

You can also change the disk usage threshold:

```
disk_threshold = 80  # in percent
```
