import requests

# Địa chỉ URL của máy chủ bạn muốn gửi dữ liệu
url = "http://example.com/api/data"  # Thay thế bằng URL thực tế của máy chủ

# Dữ liệu cần gửi (ví dụ: nhiệt độ và độ rung)
data = {
    "temperature": 22.5,
    "vibration": 0.03
}

# Gửi dữ liệu bằng phương thức POST
response = requests.post(url, json=data)

# Kiểm tra phản hồi từ máy chủ
if response.status_code == 200:
    print("Dữ liệu đã được gửi thành công!")
else:
    print("Có lỗi xảy ra:", response.status_code, response.text)
