import qrcode
import os

# 保存用フォルダの名前を定義
output_dir = 'output_pro'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# list.txt を読み込む
with open('list.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"--- 処理開始：合計 {len(lines)} 件 ---")

for i, line in enumerate(lines):
    # strip()で前後の余計な空白や改行を消す
    data = line.strip()
    
    # 1. 空行（何も書いていない行）をスキップする
    if not data:
        print(f"Skipped [{i+1}]: 空行です")
        continue
    
    # 2. try-exceptでエラーから守る
    try:
        # ファイル名を賢く作る（最初の10文字を使い、https://などは消す）
        clean_name = data.replace("https://", "").replace("www.", "").replace("/", "_")[:10]
        filename = f"{output_dir}/{i+1}_{clean_name}.png"
        
        # QRコード生成と保存
        img = qrcode.make(data)
        img.save(filename)
        print(f"Success [{i+1}]: {filename}")
        
    except Exception as e:
        # 万が一エラーが起きても、この行だけで止まらず次へ進む
        print(f"Error [{i+1}]: {data} - 理由: {e}")

print("--- すべての処理が完了しました ---")