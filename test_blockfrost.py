from blockfrost import BlockFrostApi, ApiError

# Thay thế bằng project_id của bạn
api = BlockFrostApi(project_id='previewWAg74fnxFq3yjT9U7nRQ7Fqd8Ijw0cvI')

# Địa chỉ cần kiểm tra
address_to_check = 'addr_test1qpkqvv82kppqgaaaemdhnugt63q60x7qx37sgsdwcj0chl97l89m4uzu8j74ug5v0e6wgsnda04rd7hak50whg7ly2asvz2r0d'

try:
    # Lấy thông tin địa chỉ
    address = api.address(address=address_to_check)
    print("Loại địa chỉ:", address.type)
    for amount in address.amount:
        print("Số lượng:", amount.quantity, "Đơn vị:", amount.unit)

except ApiError as e:
    print("Có lỗi xảy ra:", e)
