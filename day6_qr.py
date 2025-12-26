import qrcode

data = input("QRコードにしたい文字を入力: ")

# QRコードの設定
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# ★ ここで色を指定！ (好きな色に変えてみてください)
img = qr.make_image(fill_color="darkblue", back_color="white")

img.save('test_qr.png')
print(f"『{data}』のQRコードを青色で作成しました！")