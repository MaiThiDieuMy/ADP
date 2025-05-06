import firebase_admin
from firebase_admin import messaging, credentials
import os

FIREBASE_PATH = os.path.join(os.path.dirname(__file__), 'firebase', 'firebase-service-account.json')

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_PATH)
    firebase_admin.initialize_app(cred)

def send_fcm_v1(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )
    try:
        response = messaging.send(message)
        return True, response
    except Exception as e:
        return False, str(e)
