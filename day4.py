def judge_priority(probability):
    if probability >= 80: return "高"
    elif probability >= 50: return "中"
    return "低"

customers = [{"name": "A社", "prob": 85}, {"name": "B社", "prob": 45}]
for c in customers:
    print(f"{c['name']}: {judge_priority(c['prob'])}")