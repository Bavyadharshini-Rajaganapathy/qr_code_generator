import qrcode

qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)
urlinput = input("Enter the url: ")
qr.add_data(urlinput)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.jpg")