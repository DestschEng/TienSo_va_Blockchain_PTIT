#!/bin/bash

# Thay thế bằng project_id của bạn
PROJECT_ID="mainnetTTKmr57HqywffFOsrxn08FoSjTGC0DGs"
CBOR_FILE="/workspace/TienSo_va_Blockchain_PTIT/build/gift/script.cbor"

# Gửi yêu cầu tới Blockfrost để triển khai smart contract trên mạng mainnet
RESPONSE=$(curl -s -L -X POST 'https://cardano-mainnet.blockfrost.io/api/v0/txs/submit' \
-H 'Content-Type: application/cbor' \
-H 'Accept: application/json' \
-H "project_id: $PROJECT_ID" \
--data-binary @"$CBOR_FILE")

# In ra phản hồi từ Blockfrost
echo "Phản hồi từ Blockfrost: $RESPONSE"

# Kiểm tra mã trạng thái và lấy tx_hash nếu có
if [[ $? -ne 0 ]]; then
    echo "Có lỗi xảy ra trong quá trình gửi yêu cầu."
else
    # Lấy tx_hash từ phản hồi
    TX_HASH=$(echo "$RESPONSE" | jq -r '.hash')

    if [[ "$TX_HASH" != "null" ]]; then
        echo "Yêu cầu đã được gửi thành công! Transaction ID: $TX_HASH"

        # Kiểm tra trạng thái giao dịch
        STATUS_RESPONSE=$(curl -s -L -X GET "https://cardano-mainnet.blockfrost.io/api/v0/txs/$TX_HASH" \
        -H "project_id: $PROJECT_ID" \
        -H "Accept: application/json")

        echo "Trạng thái giao dịch: $STATUS_RESPONSE"
    else
        echo "Không thể xác nhận giao dịch. Phản hồi không hợp lệ."
    fi
fi
# chmod +x deploy_contract.sh
# ./deploy_contract.sh