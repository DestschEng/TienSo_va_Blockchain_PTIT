from pycardano import PaymentSigningKey, PaymentVerificationKey, Address, Network

# Generate payment key pair
payment_signing_key = PaymentSigningKey.generate()
payment_verification_key = PaymentVerificationKey.from_signing_key(payment_signing_key)

# Save keys to files
payment_signing_key.save("payment.skey")
payment_verification_key.save("payment.vkey")

# Create address
address = Address(payment_part=payment_verification_key.hash(), network=Network.TESTNET)
print("Your address is:", address)
