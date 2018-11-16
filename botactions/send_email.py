import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials.gmail_credentials import gmail_login
 
def send_email(user_address,message):
    msg = MIMEMultipart()
    msg['From'] = user_address
    msg['To'] = "jonathan.emil.rosado@gmail.com"
    msg['Subject'] = "[jonathanrosado.fr] Message chatbot de {}".format(user_address)
    
    body = message
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_login['account'], gmail_login['password'])
    text = msg.as_string()
    server.sendmail(gmail_login['account'], "jonathan.emil.rosado@gmail.com", text)
    server.quit()