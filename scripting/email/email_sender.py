import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("scripting/email/index.html").read_text())

email = EmailMessage()
email['from'] = "EXAMPLE USER "
email['to'] = "EXAMPLE EMAIL"
email['subject'] = "EXAMPLE SUBJECT"

email.set_content(html.substitute(name="User"), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("REPLACE YOUR EMAIL", "REPLACE YOUR PASSWORD")
    smtp.send_message(email)
    print("done")
