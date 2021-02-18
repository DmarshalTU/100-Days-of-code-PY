import smtplib
import random
import datetime as dt

EMAIL = ""
PASSWORD = ""
SEND_TO = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote:
        quotes = quote.readlines()
        qt = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SEND_TO,
            msg=f"Subject:Monday quote\n\n{qt}"
        )
