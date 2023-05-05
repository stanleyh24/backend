import httpx
from os import getenv, path
import pdfkit
import jinja2
from datetime import datetime
from database.database import get_db
from database.models import Order
#from .send_mail import Mail
from.mailer import Mail
import time
import random
import string
import subprocess

def create_invoice_name():
    s = "invoice.pdf"
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for _ in range(5))
    new= f'_{rand_str}.'
    filename = new.join(s.rsplit('.', 1))

    return f'./invoices/{filename}'

def create_invoice(order_id:str):
    db = next(get_db())
    order= db.query(Order).filter(Order.id==order_id).first()
    order.paid=True
    order.updated_At= datetime.now()
    db.commit()
    order_details = order.items
    
    Fecha = datetime.now().strftime("%d-%m-%Y")
    
    context = {
        'order': order,
        'order_details': order_details,
        'date' : Fecha
    }

    template_loader = jinja2.FileSystemLoader('./templates')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'invoice_template.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    output_pdf = create_invoice_name()
    pdfkit.from_string(output_text, output_pdf, configuration=config)
    
    send_invoice(order.email, order.first_name, output_pdf)


def confirm_payment(headers, body):
    if body['resource']['status'] == "COMPLETED":
        data = {
                "webhook_id": getenv("WEBHOOK_ID"),
                "transmission_id": headers['Paypal-Transmission-Id'],
                "transmission_time": headers['Paypal-Transmission-Time'],
                "cert_url": headers['Paypal-Cert-Url'],
                "auth_algo": headers['Paypal-Auth-Algo'],
                "transmission_sig": headers['Paypal-Transmission-Sig'],
                "webhook_event": body
            }
        r = httpx.post(getenv("VALIDATION_URL"), json=data, auth=(getenv("CLIENT_ID"),getenv("SECRET_ID")))
        
        if r.status_code == 200:
            create_invoice(body['resource']['custom_id'])


def send_invoice(mail, name, invoice_path):
    #time.sleep(5)
    """ mail = Mail()
    mail.send(mail, name, '/home/scorpion/desa/pythonprojects/backend/invoices/invoice_jFSMZ.pdf') """
    subprocess.run(["python3", "./utils/mailer.py", mail,name,invoice_path])


def slugify(word):
    return "-".join(word.split()).lower()