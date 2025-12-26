import qrcode
import os

# 保存用フォルダがなければ作る
if not os.path.exists('output'):
    os.makedirs('output')

# list.txtを一行ずつ読み込む
with open('list.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    url = line.strip() # 改行などを取り除く
    if not url:
        continue
        
    img = qrcode.make(url)
    filename = f"output/qr_{i+1}.png"
    img.save(filename)
    print(f"{filename} を作成しました: {url}")