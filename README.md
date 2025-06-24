# 💧 Drink Water Reminder (Python Script)

![Water Reminder](https://m.media-amazon.com/images/I/614bT4bkDCL.png)

A simple yet effective Python script to remind you to stay hydrated by sending desktop notifications every hour.

## 🚀 Features

- Sends desktop notifications every 60 minutes  
- Lightweight and minimal  
- Works on Windows, macOS, and Linux

## 📦 Requirements

Make sure you have Python installed. Install the plyer module using:  
`pip install plyer`

## 🧠 How It Works

The script runs an infinite loop and sends a hydration reminder every hour using your system's native notification system via the plyer library.

## 💻 Code

The script uses the time and plyer modules. It prints a message to the terminal and shows a system notification every hour.
Leave it running in the background — you'll receive a reminder every hour!

## 🛠 Optional Customization

Want reminders more frequently? You can change the interval by adjusting the `time.sleep` value. For example, to get reminders every 30 minutes instead of 60, change `60 * 60` to `60 * 30`.

## 🧃 Stay Hydrated!

This is a simple self-care script to remind you that your health matters. Run it in the background, drink regularly, and feel refreshed! 💙
