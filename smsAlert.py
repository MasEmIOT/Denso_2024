from twilio.rest import Client

# Thông tin tài khoản Twilio
account_sid = 'your_account_sid'  # Từ Twilio
auth_token = 'your_auth_token'      # Từ Twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Cảnh báo: Điều kiện bất thường như quá nhiệt!',
    from_='+1234567890',  # Số điện thoại Twilio của bạn
    to='+0987654321'      # Số điện thoại người nhận
)

print(f"SMS sent successfully! Message SID: {message.sid}")
