import smtplib
from email.mime.text import MIMEText

# Your email credentials and server information
email_address = "zpalasti@aol.com"
email_password = "IBM88ibm"
smtp_server = "smtp.aol.com"
smtp_port = 465  # Use 587 for TLS or 465 for SSL

# Create an SMTP_SSL object
server = smtplib.SMTP_SSL(smtp_server, smtp_port)

# Log in to your AOL email account
server.login(email_address, email_password)

# Create a simple email message
message = MIMEText("Hello, this is a test email.")
message["Subject"] = "Test Email"
message["From"] = email_address
message["To"] = "zpalasti@aol.com"

# Send the email
server.sendmail(email_address, "zpalasti@aol.com", message.as_string())

# Quit the server
server.quit()

