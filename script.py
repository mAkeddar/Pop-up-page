import qrcode

# URL of the hosted HTML page
page_url = "https://yourdomain.com/location_page.html"

# Generate the QR code
qr = qrcode.make(page_url)

# Save the QR code as an image
qr.save("location_qr_code.png")
