##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



import datetime as dt
import random
import smtplib
import pandas

my_email=my_email
password=password

#check if today matches a birthday in the birthdays.csv
date_now=dt.datetime.now()
current_month=date_now.month
current_day=date_now.day

filename=['letter_1.txt','letter_2.txt','letter_3.txt']

# Use pandas to read the birthdays.csv
birthday_file=pandas.read_csv('./birthdays.csv')
birthday_dict=birthday_file.to_dict()
birthday_month=[row['month'] for (index,row) in birthday_file.iterrows()]
birthday_day=[row['day'] for (index,row) in birthday_file.iterrows()]
print(birthday_dict)

for item in range(len(birthday_day)):
    if current_day == birthday_day[item] and current_month == birthday_month[item]:
        random_file=random.choice(filename)
        with open (f'./letter_templates/{random_file}') as file:
            data=file.read()
            data=data.replace("[NAME]",birthday_dict['name'][item])
            print(data)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{birthday_dict['email'][item]}",
                msg=f"Subject:Happy Birthday\n\n {data}"
            )





