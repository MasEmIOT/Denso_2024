import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Chế độ đánh số chân BCM
sensor_pin = 4  # Thay đổi với chân mà bạn đã kết nối cảm biến

GPIO.setup(sensor_pin, GPIO.IN)  # Thiết lập chân GPIO làm đầu vào

try:
    while True:
        sensor_value = GPIO.input(sensor_pin)  # Đọc giá trị từ cảm biến
        print("Giá trị cảm biến:", sensor_value)
        time.sleep(1)  # Đợi 1 giây

except KeyboardInterrupt:
    GPIO.cleanup()  # Dọn dẹp chân GPIO
-	Step 5 (thiết lập Node – Red Flow)
•	Mở giao diện node – red : truy cập http://<IP của Raspberry Pi>:1880
•	Tạo flow để đọc dữ liệu từ cảm biến  
o	Node Inject: Để thử nghiệm, bạn có thể sử dụng Inject để tạo tín hiệu giả lập dữ liệu cảm biến.
o	 Node Function: Sử dụng node này để xử lý dữ liệu. Ví dụ: nếu bạn đọc nhiệt độ và cần cảnh báo khi nhiệt độ vượt quá một mức nhất định, bạn có thể xử lý điều này tại đây.
Ví dụ, để kiểm tra nhiệt độ
if (msg.payload > 70) {
    msg.payload = "Cảnh báo: Nhiệt độ quá cao!";
} else {
    msg.payload = "Nhiệt độ bình thường: " + msg.payload + "°C";
}
return msg;
