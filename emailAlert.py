
import smtplib
from email.mime.text import MIMEText

# Thiết lập thông tin email
sender_email = "your-email@gmail.com"
receiver_email = "recipient@example.com"
password = "your-email-password"

# Tạo nội dung email
subject = "Cảnh báo: Điều kiện bất thường!"
body = "Đã phát hiện điều kiện bất thường như quá nhiệt!"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Gửi email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
