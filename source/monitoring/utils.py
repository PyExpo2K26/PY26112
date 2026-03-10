from twilio.rest import Client
from django.conf import settings

def send_sms_alert(phone_number, village, cause, remedy):
    """
    Sends an SMS alert using Twilio.
    Returns True if successful, False otherwise.
    """
    if not getattr(settings, 'TWILIO_ACCOUNT_SID', None) or not getattr(settings, 'TWILIO_AUTH_TOKEN', None):
        print("Twilio credentials not configured.")
        return False
        
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message_body = (
            f"WATER ALERT: Contamination detected in {village}.\n"
            f"Cause: {cause}\n"
            f"Remedy: {remedy}\n"
            f"Please take immediate action."
        )
        
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        print(f"SMS sent successfully: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return False
