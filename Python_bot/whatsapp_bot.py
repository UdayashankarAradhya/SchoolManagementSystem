from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# Your Twilio credentials

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello from your School Management System chatbot!',
    from_='whatsapp:+14155238886',  # Your Twilio sandbox WhatsApp number
    to='whatsapp:+917483714365'  # Your WhatsApp number where you want to receive messages
)

print(f"Message SID: {message.sid}")
