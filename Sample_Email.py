import smtplib

my_email = "krishnabodepu24@gmail.com"
pwd = "fbzjhkarsfqoajvg"  # need to generate APP Password by turning on 2-step authentication in the gmail

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=pwd)

message = """From: <krishnabodepu24@gmail.com>
To: <krishanbodepu@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
# another method for message
# message = """From: From <Person Name><krishnabodepu24@gmail.com>
# To: To <To Person><krishanbodepu@gmail.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """

connection.sendmail(from_addr=my_email,
                    to_addrs='krishanbodepu@gmail.com',
                    msg=message)

connection.close()
