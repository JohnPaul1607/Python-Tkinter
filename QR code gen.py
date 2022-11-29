import pyqrcode
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://chat.whatsapp.com/CCqGn8vxAmU7gM65e5bg9J"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("LINK.svg", scale = 8) 
