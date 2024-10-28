import qrcode

# URL of the hosted HTML page
page_url = "https://makeddar.github.io/Pop-up-page/"

# Generate the QR code
qr = qrcode.make(page_url)

# Save the QR code as an image
qr.save("location_qr_code.png")
