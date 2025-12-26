import pandas as pd
import qrcode
import os

# 1. データの読み込み
df = pd.read_csv('data.csv')

# 2. フォルダ作成
output_dir = 'output_pandas'
os.makedirs(output_dir, exist_ok=True)

print("--- データの中身を表示 ---")
print(df)
print("-----------------------")

# 3. Pandasの機能で1行ずつ処理
for index, row in df.iterrows():
    url = str(row['url']).strip()
    name = str(row['name']).strip()
    
    # 名前が空（NaN）の場合は「no_name」にする
    if name == 'nan' or not name:
        name = "no_name"
    
    try:
        img = qrcode.make(url)
        filename = f"{output_dir}/{row['id']}_{name}.png"
        img.save(filename)
        print(f"成功: {filename}")
    except Exception as e:
        print(f"失敗: {row['id']} - {e}")

print("\nすべて完了！Pandasでの一括処理に成功しました。")