
import smtplib
import random
import datetime as dt

my_email = my_email
password=password

now=dt.datetime.now()
weekday=now.weekday()

if weekday == 3:

    with open ('./quotes.txt') as file:
        data=file.readlines()
        random_quotes=random.choice(data)
        print(random_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email
            msg=f"Subject:Thursday Motivation\n\n {random_quotes}"
        )
