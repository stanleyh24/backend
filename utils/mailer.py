import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import sys

class Mail:

    def __init__(self):
        self.port = 1025
        self.smtp_server_domain_name = "localhost"
        self.sender_mail = "stan@gmail.com"
        self.password = ""

    def send(self,to_email,name,invoice_path):
        msg = MIMEMultipart()

        html_template = """
            <h1>Caoba Cigars</h1>

            <p>Hola {0},</p>
            <p>Gracias por preferir los productos de <b>Caoba Cigars</b>.</p>
            """

        message = "Test Message"
        msg['From'] = self.sender_mail
        msg['To'] = to_email
        msg['Subject'] = "Factura Caoba Cigars"

        msg.attach(MIMEText(html_template.format(name),'html'))

        file_path = invoice_path
        if (Path(file_path).exists()):
            mimeBase = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as file:
                mimeBase.set_payload(file.read())
            encoders.encode_base64(mimeBase)
            mimeBase.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
            msg.attach(mimeBase)

        server =smtplib.SMTP(self.smtp_server_domain_name,self.port) 
        #server.starttls()
        server.login("","")
        server.sendmail(msg['From'],msg['To'],msg.as_string())

        server.quit()

        print (f"successfully sent email to :{msg['To']}")



if __name__ == "__main__":
    m = Mail()
    m.send(sys.argv[1],sys.argv[2],sys.argv[3])