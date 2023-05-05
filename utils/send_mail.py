import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from os import getenv


class Mail:

    """ def __init__(self):
        self.port = getenv("SMTP_PORT")
        self.smtp_server_domain_name = getenv("SMTP_SERVER_DOMAIN_NAME")
        self.sender_mail = getenv("EMAIL_SENDER")
        self.password = getenv("EMAIL_PASSWORD") """
    def __init__(self):
        self.port = 1025
        self.smtp_server_domain_name = "localhost"
        self.sender_mail = "stan@gmail.com"
        self.password = ""
        
    def send(self,email, name , invoice_path):
        mail = MIMEMultipart()
        mail['Subject'] = 'Factura Caoba Cigars'
        mail['From'] = self.sender_mail
        mail['To'] = email

        text_template = """
            Caoba Cigars

            Hi {0},
            We are delighted announce that our website hits 10 Million views this month.
            """

        html_template = """
            <h1>Caoba Cigars</h1>

            <p>Hola {0},</p>
            <p>Gracias por preferir los productos de <b>Caoba Cigars</b>.</p>
            """

        html_content = MIMEText(html_template.format(name), 'html')
        #text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')

        #mail.attach(text_content)
        mail.attach(html_content)
            
            
        file_path = invoice_path
        print(Path(file_path).exists())
        """ if (Path(file_path).exists()):
            mimeBase = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as file:
                mimeBase.set_payload(file.read())
            encoders.encode_base64(mimeBase)
            mimeBase.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
            mail.attach(mimeBase) """

        server = smtplib.SMTP(host=self.smtp_server_domain_name, port=self.port)
        #server.ehlo()
        #server.starttls()
        #server.login(self.sender_mail, self.password)
        server.login("", "")
        server.sendmail(self.sender_mail, email, mail.as_string())

        server.quit()
