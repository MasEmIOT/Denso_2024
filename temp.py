if temperature > MAX_TEMPERATURE:  # MAX_TEMPERATURE là ngưỡng tối đa mà bạn đã định nghĩa
    send_alert()  # Gọi hàm để gửi cảnh báo
-	Phương thức gửi cảnh báo: sử dụng thư viện smtplib để gửi email cảnh báo tới người quản lý hoặc kỹ thuật viên
import smtplib

def send_email_alert(temperature):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    message = f"Warning: Temperature too high! Current temperature: {temperature:.1f}°C"
    server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", message)
    server.quit()
