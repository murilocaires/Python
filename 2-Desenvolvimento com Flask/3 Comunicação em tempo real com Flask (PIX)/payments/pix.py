import uuid
import qrcode

class Pix():
    def __init__(self):
        pass
    def create_payment(self, base_path=""):
        #cria uma id ficticio de uama trasação com uma intituição financeira
        bank_payment_id = str(uuid.uuid4())

        #cria o copia e cola do pagamento
        hash_payment = f'hash_payment_{bank_payment_id}'

        #cria o qrcode
        img  = qrcode.make(hash_payment)

        #salva a imagem do qrcode
        img.save(f'{base_path}static/img/qr_code_payment_{hash_payment}.png')

        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f'qr_code_payment_{hash_payment}'}