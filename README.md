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

## Configuration

Edit the script to set your Slack webhook URL:

```
webhook_url = '<slack webhook url>'
```

You can also change the disk usage threshold:

```
disk_threshold = 80  # in percent
```
## Usage

Run the script using:
```
python disk_monitor.py
```

it will:

Continuously check the disk usage every 20 minutes.
Send a message to your Slack channel if usage exceeds the threshold.

## How It Works

- Uses psutil to get disk usage statistics.
- Compares usage with a pre-defined threshold.
- Sends alerts via requests to a Slack webhook.
- Uses asyncio to manage wait times without blocking execution.

## Example Notification
```
The disk on host ---[ my-hostname ]--- is 91% full! Please free up some space.
```
### Security Tip

Do not expose your Slack webhook URL publicly. Keep it in environment variables or secured configuration files in production.
