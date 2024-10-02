import Adafruit_DHT

# Đặt loại cảm biến và chân GPIO
sensor = Adafruit_DHT.DHT22
pin = 4  # Chân GPIO kết nối cảm biến

# Đọc dữ liệu từ cảm biến
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f'Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%')
else:
    print('Failed to retrieve data from the sensor')
