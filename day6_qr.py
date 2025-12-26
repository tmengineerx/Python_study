import qrcode

# ユーザーから入力を受け取る
data = input("QRコードにしたい文字やURLを入力してください: ")

img = qrcode.make(data)
img.save('test_qr.png')

print(f"QRコード『test_qr.png』を作成しました！（中身: {data}）")