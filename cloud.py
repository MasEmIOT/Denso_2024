import requests

url = 'https://your-cloud-endpoint.com/api/data'  # Thay đổi địa chỉ endpoint của bạn
data = {
    'temperature': 25,
    'humidity': 60
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Dữ liệu đã được gửi thành công!')
else:
    print('Có lỗi xảy ra:', response.status_code)

