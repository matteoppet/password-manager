from flask import redirect, session

from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return wrap



from cryptography.fernet import Fernet
import base64


cipher_suite = Fernet(base64.urlsafe_b64encode(b'12345678901234567890123456789012'))
encoding = "utf-8"


def encryption(messageToEncrypt):
    
    messageToEncode = bytes(messageToEncrypt, encoding)

    encryptedMessage = cipher_suite.encrypt(messageToEncode)

    return encryptedMessage


def decryption(messageToDecrypt):
    
    decryptedMessage = cipher_suite.decrypt(messageToDecrypt)

    return decryptedMessage