import qrcode
file_path = "index.html"

with open(file_path, "rb") as file:
    html_data = file.read()
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(html_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("qr_code.png")