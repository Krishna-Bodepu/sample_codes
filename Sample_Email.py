import smtplib

my_email = "krishnabodepu24@gmail.com"
pwd = "hvkqhhhwhpqnceuv" # need to generate APP Password by turning on 2-step authentication in the gmail

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=pwd)

connection.sendmail(from_addr=my_email,
                    to_addrs='krishanbodepu@gmail.com',
                    msg='Hi Krishna, this is a test email')

connection.close()
