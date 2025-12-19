import qrcode
from datetime import datetime
from PIL import Image


# Ask user for input
data = input("Enter the text or URL for the QR code: ")

qr = qrcode.make(data)

# Generate a unique filename using timestamp
filename = f"Qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

# Save QR code
qr.save(filename)

# Open the saved image automatically
img = Image.open(filename)
img.show()

print(f"QR code saved as: {filename}")