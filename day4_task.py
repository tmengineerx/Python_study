import pandas as pd

# 1. 営業リストの作成（データの準備）
data = {
    '顧客名': ['A商事', 'B工業', 'C小売', 'D建設', 'E不動産'],
    '成約確率': [90, 40, 75, 20, 55]
}

# 2. 表形式（DataFrame）に変換
df = pd.DataFrame(data)

# 3. 優先度判定のロジックを「関数」として定義
def judge_priority(prob):
    if prob >= 80: return "高（即連絡）"
    elif prob >= 50: return "中（フォロー）"
    return "低（様子見）"

# 4. 新しい列「優先度」を追加（関数を適用）
df['優先度'] = df['成約確率'].apply(judge_priority)

# 5. CSVファイルとして保存
df.to_csv('customer_list_day4.csv', index=False, encoding='utf-8-sig')

print("--- 処理完了 ---")
print(df) # 画面にも表を表示