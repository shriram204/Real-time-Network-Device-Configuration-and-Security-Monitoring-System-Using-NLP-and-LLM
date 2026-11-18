import smtplib
from email.mime.text import MIMEText def send_email_alert(message):
sender = "ai.network.alert@gmail.com" password = "ckkwkfvdqyuueqru" receiver = "mapsal2608@gmail.com" msg = MIMEText(message)
msg["Subject"] = "Network Intrusion Alert" msg["From"] = sender
msg["To"] = receiver
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: server.login(sender, password)
 
server.sendmail(sender, receiver, msg.as_string())
