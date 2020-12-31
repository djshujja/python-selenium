from twilio.rest import Client


account_sid = "AC3ccee2569f6c9e72707498f2af12d551"
auth_token = "b0bf61f7eb31a4fd97bb82f6aca8264b"
phone_number = "+19388884001"
my_phone="+923005067673"

client = Client(account_sid, auth_token)

client.messages.create(
    to=my_phone,
    from_=phone_number,
    body="Hello from Python, Shujja!"
)