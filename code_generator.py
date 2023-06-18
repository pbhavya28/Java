import qrcode
qr_code=qrcode.QRCode(version=15,box_size=10,border=5)
data="https://www.linkedin.com/in/bhavya-patel-ce/"
qr_code.add_data(data)
qr_code.make(fit=True)
img=qr_code.make_image(fill="black",back_color="black")
img.save('qrcode.png')
