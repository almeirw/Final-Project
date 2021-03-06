import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = input("Email:")
password = input("Password:")
# code untuk mendapatkan library yang menghubungkan email
# https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/

subject = input("Subject:")
body = input("Message:")

msg = f"""Subject: {subject}\n\n{body}"""
# code untuk memisahkan subject dengan body email
# https://stackoverflow.com/questions/57102614/sending-gmail-emails-through-python-smtplib-cant-separate-body-from-subject

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    with open("receiver_list.txt", "r") as file:
        x = file.readlines()
        server.sendmail(sender_email, x, msg)
        # code untuk menghubungkan server SMTP
        # https://realpython.com/python-send-email/
print('Email has been sent')
