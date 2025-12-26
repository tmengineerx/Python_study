import qrcode

# 1. QRコードにしたい情報（例えば自社の紹介ページや、顧客IDなど）
data = "https://www.google.com" # ここを自由に変えられます

# 2. QRコードの生成
img = qrcode.make(data)

# 3. 画像として保存
img.save("test_qr.png")

print("QRコード『test_qr.png』を作成しました！")