#pip install pix Qr Code
from pixqrcode import PixQrCode

name = "Name"
mobile = "(xx) xxxxx-xxxx"
city = "City"
amount = "0000,00"

# Param: name, mobile, city, amount, referencial code
pix = PixQrCode(name, mobile, city, amount)

#base 64 export
pix.export_base64()

#.png default save
pix.save_qrcode("./","Name_File")