import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import time as t
import json

# Set up email details
day = date.today()
current_time = t.strftime("%I:%M:%S %p")
credentials_file='/home/saim/PycharmProjects/practice/venv/credential.json'

path = '/home/saim/PycharmProjects/practice/venv/TFI ORGANICS AUTOMATICS EMAIL SENDER/emails.csv'
sender_email = "info@tfiorganics.com"

with open(credentials_file, 'r') as cred:
    my_dict=json.load(cred)

password = my_dict[0]["password"]

# Read recipient emails
with open(path, 'r') as f:
    receiver_email_list = [line.strip() for line in f if line.strip()]

# Email content
subject = 'Quality Himalayan Salt Products from TFI Organics'
body = '''
Dear Sir/Madam,

I hope this message finds you well.

I’m reaching out to introduce TFI Organics, a Karachi-based company specializing in high-quality Himalayan salt products. You can learn more about us at our website: https://www.tfiorganics.com.

At TFI Organics, we understand the growing demand for Himalayan salt worldwide. Our commitment to quality has allowed us to establish strong partnerships with local salt mines in the Himalayan region. This ensures that we provide ethically sourced and sustainable products to our clients.

Our product range includes:
- Edible Himalayan salt
- Black salt
- De-icing salt products

We are dedicated to meeting the diverse needs of our customers and would love to discuss how we can support your requirements.

Feel free to visit our website for more details or reach out if you have specific questions or needs.

Looking forward to your response!

Best regards,
Talha Feroz
TFI Organics
Sector 6A Plot Number A309 Mehran Town, K.I.A, Karachi
UK Office: Office #3, 117 A George Lane South Woodford, London E18 1AU
+92 345 2005052 (WhatsApp)
+92 300 364 9929
info@tfiorganics.com
'''

# Establish the SMTP connection
try:
    connection = smtplib.SMTP('smtpout.secureserver.net')
    connection.starttls()
    connection.login(user=sender_email, password=password)

    # Loop through each recipient
    for receiver_email in receiver_email_list:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))  # Change 'plain' to 'html' if using HTML

        connection.send_message(msg)
        print(f"Mail sent to {receiver_email}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    connection.quit()
