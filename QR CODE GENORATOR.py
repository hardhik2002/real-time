import qrcode

features = qrcode.QRCode(version=1, box_size=45, border=3)
features.add_data("https://samvidha.iare.ac.in/")
features.make(fit=True)
genarate_image = features.make_image(fill_color="black", back_color="white")
genarate_image.save("qrcode2.png")

