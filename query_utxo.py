from blockfrost import BlockFrostApi, ApiError, ApiUrls

# Set your Blockfrost project ID
project_id = "preview9PXxs5Nyq2gySWKOyojeNoOuVJvqOvjg"
api = BlockFrostApi(project_id=project_id, base_url=ApiUrls.preview.value)

# Replace with your address
address = "addr_test1vrn20j76s3qxasjwuh60pjxzhkfraywj4k683uzal6sccugq4q7um"

try:
    utxos = api.address_utxos(address)
    print("UTXOs for address:", address)
    for utxo in utxos:
        print(utxo)
except ApiError as e:
    print(e)
