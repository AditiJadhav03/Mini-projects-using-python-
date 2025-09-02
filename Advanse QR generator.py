import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Take input from user
data = input("Enter text or link for QR Code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size (1 = small, 40 = large)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box
    border=4,     # border thickness
)
qr.add_data(data)
qr.make(fit=True)

# Make fancy QR without external logo file
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),  # rounded box style
    color_mask=RadialGradiantColorMask(   # cool gradient effect
        center_color=(0, 100, 255),       # blue in middle
        edge_color=(0, 0, 0)              # black edges
    )
)

# Save QR Code
img.save("fancy_qr.png")
print("QR Code generated and saved as fancy_qr.png")

