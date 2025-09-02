''' this is simple QR code generator script '''

import qrcode

data = input("Enter text/URL for QR Code: ")
qr = qrcode.make(data)
qr.save("my_qrcode.png")
print("QR Code saved as my_qrcode.png")