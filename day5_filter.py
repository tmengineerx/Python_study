import pandas as pd

# 1. データの準備（昨日のリストを少し増やしました）
data = {
    '顧客名': ['A商事', 'B工業', 'C小売', 'D建設', 'E不動産', 'F商事', 'Gテック'],
    '成約確率': [90, 40, 75, 20, 55, 95, 30]
}
df = pd.DataFrame(data)

# 2. 【今日のメイン】条件に合うデータだけを抜き出す
# 成約確率が 70% 以上の顧客だけを抽出
high_prob_df = df[df['成約確率'] >= 70]

# 3. 画面で確認
print("--- 成約確率70%以上のリスト ---")
print(high_prob_df)

# 4. 抽出結果だけを新しいCSVに保存
high_prob_df.to_csv('high_priority_list.csv', index=False, encoding='utf-8-sig')
print("\n高精度リストを保存しました。")