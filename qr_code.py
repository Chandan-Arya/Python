# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represent the QR code
site = "https://www.chandanarya.in"

# Generate the QR code
url_qr = pyqrcode.create(site)

# Create and save the svg file naming "myqr.svg"
url_qr.svg("chandanarya.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url_qr.png("chandanarya.png", scale= 6)