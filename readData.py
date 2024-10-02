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

