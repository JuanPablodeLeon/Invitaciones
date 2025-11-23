import qrcode

url = input("Enter URL: ").strip()
file_path = "E:\\juanp\\Documents\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Creado")