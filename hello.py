import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "day18 学習ログ生成"
    
    # 部品の作成
    task_input = ft.TextField(label="タスクを改行して入力", multiline=True, min_lines=3)
    log_output = ft.TextField(label="生成結果", multiline=True, read_only=True)

    def generate_log(e):
        if not task_input.value: return
        
        # 1. 12/23をday1とした計算
        start = datetime(2025, 12, 23)
        day_count = (datetime.now() - start).days + 1
        
        # 2. 【最重要】複数行をバラバラにして[x]を付ける処理
        lines = task_input.value.splitlines()
        formatted_list = [f"[x] {line.strip()}" for line in lines if line.strip()]
        tasks_text = "\n".join(formatted_list)
        
        # 3. 組み立て
        log_output.value = (
            f"day{day_count}/Python基礎：繰り返し処理\n"
            f"📅 日付: {datetime.now().strftime('%Y-%m月%d日')}\n\n"
            f"✅ 実施済みタスク\n{tasks_text}\n\n"
            f"📝 習得スキル: for文(内包表記), splitlines()"
        )
        page.update()

    page.add(
        ft.Text("学習ログ作成 (day18版)", size=20, weight="bold"),
        task_input,
        ft.ElevatedButton("ログ生成", on_click=generate_log),
        log_output
    )

if __name__ == "__main__":
    ft.app(target=main)