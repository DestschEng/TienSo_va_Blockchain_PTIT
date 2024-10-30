import requests

# Thay thế bằng project_id của bạn
project_id = "mainnetUx1tebW5uyoIXvyKsq3lzquWb8P4q4Oy"

# Đọc file script.cbor
with open("/workspace/TienSo_va_Blockchain_PTIT/build/gift/script.cbor", "rb") as f:
    cbor_data = f.read()

# Đọc địa chỉ testnet
with open("/workspace/TienSo_va_Blockchain_PTIT/build/gift/testnet.addr", "r") as f:
    address = f.read().strip()

# Gửi yêu cầu tới Blockfrost để triển khai smart contract
url = f"https://cardano-mainnet.blockfrost.io/api/v0/txs/submit"
headers = {
    "project_id": project_id,
    "Content-Type": "application/json",
}

# Chuẩn bị dữ liệu cho transaction
data = {
    "cbor": cbor_data.hex(),  # Chuyển đổi CBOR sang dạng hex
}

# In thông tin yêu cầu
print(f"Gửi yêu cầu tới: {url}")
print("Dữ liệu gửi đi:", data)

response = requests.post(url, headers=headers, json=data)

# Kiểm tra phản hồi từ Blockfrost
if response.status_code == 200:
    print("Smart contract đã được triển khai thành công!")
    print("Chi tiết giao dịch:", response.json())
else:
    print(f"Có lỗi xảy ra khi triển khai smart contract: {response.status_code}")
    print("Phản hồi từ Blockfrost:", response.text)
