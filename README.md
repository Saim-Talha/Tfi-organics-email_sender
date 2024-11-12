# TFI Organics Automated Email Sender

This project is an automated email sender built using Python, designed to facilitate mass email communication for TFI Organics. It reads recipient emails from a CSV file and sends a preformatted message to each recipient using SMTP. This tool is ideal for sending updates, newsletters, and promotional emails.

## Features
- **Automated email delivery**: Sends personalized emails to multiple recipients from a CSV file.
- **SMTP support**: Configured to work with `smtpout.secureserver.net` server.
- **JSON credential handling**: Stores sender email credentials securely in a JSON file.
- **Plain text and HTML compatibility**: Customize the email format.

## Example Output
- Mail sent to recipient@example.com
- Mail sent to another@example.com
## Prerequisites
- Python 3
- Required packages: `smtplib`, `email`, `json`, `datetime`