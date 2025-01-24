import smtplib

my_email = "ajnight124@gmail.com"
password = "ajnight124"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="agauro@myseneca.ca", msg="Subject:Hello\n\nThis is the body of my email")