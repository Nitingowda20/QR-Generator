import qrcode
from datetime import datetime
from PIL import Image

data = "https://www.youtube.com/shorts/4JQsO91ZY8Q"

qr = qrcode.make(data)

# Generate a unique filename using timestamp
filename = f"Qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

# Save QR code
qr.save(filename)

# Open the saved image automatically
img = Image.open(filename)
img.show()

print(f"QR code saved as: {filename}")