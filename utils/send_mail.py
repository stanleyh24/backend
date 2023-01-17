import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path


class Mail:

    def __init__(self):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "ventas@caobacigars.com"
        self.password = "gZh4X5kRvDj4KRW"

    def send(self, emails):
        server = smtplib.SMTP(host=self.smtp_server_domain_name, port=self.port)
        server.ehlo()
        server.starttls()
        server.login(self.sender_mail, self.password)
        
        for email in emails:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = 'Caoba Cigars'
            mail['From'] = self.sender_mail
            mail['To'] = email

            text_template = """
            Caoba Cigars

            Hi {0},
            We are delighted announce that our website hits 10 Million views this month.
            """

            html_template = """
            <h1>Caoba Cigars</h1>

            <p>Hi {0},</p>
            <p>We are delighted announce that our website hits <b>10 Million</b> views last month.</p>
            """

            html_content = MIMEText(html_template.format(email.split("@")[0]), 'html')
            text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')

            mail.attach(text_content)
            mail.attach(html_content)
            
            
            file_path = './invoices/invoice_asd.pdf'
            mimeBase = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as file:
                mimeBase.set_payload(file.read())
            encoders.encode_base64(mimeBase)
            mimeBase.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
            mail.attach(mimeBase)

            server.sendmail(self.sender_mail, email, mail.as_string())

        server.quit()
        print("Email sent successfully")