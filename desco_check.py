import requests
import smtplib
import os

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

# Change threshold here
#
# Example:
# 100 = alert below 100 BDT
# 200 = alert below 200 BDT
# 50  = alert below 50 BDT

THRESHOLD = 380

# =====================================================
# EMAIL RECEIVERS
# =====================================================

TO_EMAILS = [
    "fazlerabbii2000@gmail.com",
    "messi236167@gmail.com",
    "fazlerabbicse65@gmail.com",
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

    reading_time = result["data"]["readingTime"]

    print(
        f"Current Balance: {balance} BDT"
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

This is an automatic DESCO prepaid balance notification.

Account No : {ACCOUNT_NO}

Meter No   : {METER_NO}

Current Balance : {balance} BDT

Threshold Set   : {THRESHOLD} BDT

Reading Time : {reading_time}

Your DESCO prepaid meter balance has dropped below 100 BDT.

Please recharge your meter as soon as possible to avoid any unexpected power interruptions.

Regards,
DESCO Balance Monitor created by Md Fazley Rabbi
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
                    f"Failed to send "
                    f"to {receiver}"
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
