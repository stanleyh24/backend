from fastapi import  Request

def create_invoice():
    pass


def confirm_payment(headers, body):
    if body['resource']['status'] == "COMPLETED":
        print(headers)
        print(body['resource']['amount']['value'])
        #print(body['resource']['custom_id'])



def send_invoice():
    pass


def slugify(word):
    return "-".join(word.split()).lower()