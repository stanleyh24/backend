import httpx
from os import getenv
import pdfkit
import jinja2
from datetime import datetime
from database.database import get_db
from database.models import Order
from .send_mail import Mail
import time

def create_invoice(order_id:str):
    order= next(get_db()).query(Order).filter(Order.id==order_id).first()
    order_datails = order.items
    
    Fecha = datetime.now().strftime("%d-%m-%Y")
    
    context = {
        'order': order,
        'order_datails': order_datails,
        'date' : Fecha
    }

    template_loader = jinja2.FileSystemLoader('./templates')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'invoice_template.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    output_pdf = './invoices/invoice_asd.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config)
    
    #send_invoice([order.email,])


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
            print("Success")
            print(body['resource']['custom_id'])
            create_invoice(body['resource']['custom_id'])


def send_invoice(mails):
    time.sleep(10)
    mail = Mail()
    mail.send(mails)


def slugify(word):
    return "-".join(word.split()).lower()