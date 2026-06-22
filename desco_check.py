import requests
import smtplib
import os

from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

# =====================================================
# DESCO SETTINGS
# =====================================================

ACCOUNT_NO = "21000736"
METER_NO = "066120003770"

# =====================================================
# ALERT SETTINGS
# =====================================================

THRESHOLD = 400

# =====================================================
# EMAIL RECEIVERS
# =====================================================

TO_EMAILS = [
    "fazlerabbii2000@gmail.com",
    "abdullahalfaraby7@gmail.com"
]

# =====================================================
# DESCO API
# =====================================================

URL = (
    "https://prepaid.desco.org.bd/api/tkdes/customer/"
    f"getBalance?accountNo={ACCOUNT_NO}&meterNo={METER_NO}"
)

try:

    response = requests.get(
        URL,
        timeout=30,
        verify=False
    )

    response.raise_for_status()

    result = response.json()

    balance = float(
        result["data"]["balance"]
    )

    reading_time_raw = result["data"]["readingTime"]

    dt = datetime.strptime(
        reading_time_raw,
        "%Y-%m-%d %H:%M:%S"
    )

    reading_time = dt.strftime(
        "%d %b %Y, %I:%M:%S %p"
    )

    # Current script run time
    current_time = datetime.now().strftime(
        "%d %b %Y, %I:%M:%S %p"
    )

    print(
        f"Current Balance: {balance} BDT"
    )

    print(
        f"DESCO Reading Time: {reading_time}"
    )

    print(
        f"Current Time: {current_time}"
    )

    # =================================================
    # ALERT CONDITION
    # =================================================

    if balance <= THRESHOLD:

        print(
            "Low balance detected. Sending email..."
        )

        sender_email = os.environ["EMAIL_USER"]

        sender_password = os.environ["EMAIL_PASS"]

        subject = (
            f"⚠ DESCO Low Balance Alert "
            f"({balance} BDT)"
        )

        body = f"""
Hello,

⚠️ This is an automated DESCO prepaid balance alert.

DESCO Account Details
────────────────────
Account No : {ACCOUNT_NO}
Meter No : {METER_NO}

Current Status
────────────────────
Current Balance : {balance} BDT
Alert Threshold : {THRESHOLD} BDT
DESCO Reading Time : {reading_time}
Alert Generated At : {current_time}

Your DESCO prepaid meter balance has dropped below {THRESHOLD} BDT.
Please recharge your meter as soon as possible to avoid any unexpected power interruptions.

Regards,
DESCO Balance Monitor
Created by Md Fazley Rabbi
"""

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        for receiver in TO_EMAILS:

            try:

                msg = MIMEMultipart()

                msg["From"] = sender_email
                msg["To"] = receiver
                msg["Reply-To"] = sender_email
                msg["Subject"] = subject
                msg["X-Mailer"] = (
                    "DESCO Balance Monitor"
                )
                msg["X-Priority"] = "3"

                msg.attach(
                    MIMEText(
                        body,
                        "plain"
                    )
                )

                server.sendmail(
                    sender_email,
                    receiver,
                    msg.as_string()
                )

                print(
                    f"Alert sent to {receiver}"
                )

            except Exception as e:

                print(
                    f"Failed to send to {receiver}"
                )

                print(e)

        server.quit()

    else:

        print(
            f"Balance OK "
            f"({balance} BDT > {THRESHOLD} BDT)"
        )

except Exception as e:

    print(
        "ERROR:",
        e
    )

    raise
