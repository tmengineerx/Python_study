import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "day19 学習ログ保存アプリ"
    
    # 部品の作成
    task_input = ft.TextField(label="タスクを改行して入力", multiline=True, min_lines=3)
    log_output = ft.TextField(label="生成結果", multiline=True, read_only=True)

    def generate_log(e):
        if not task_input.value:
            return
        
        # 1. 計算（ここが消えていたので NameError になっていました）
        start = datetime(2025, 12, 23)
        day_count = (datetime.now() - start).days + 1
        
        # 2. タスク整形
        lines = task_input.value.splitlines()
        formatted_list = [f"[x] {line.strip()}" for line in lines if line.strip()]
        tasks_text = "\n".join(formatted_list)
        
        # 3. 組み立て
        log_content = (
            f"day{day_count}/Python基礎：ファイル操作の実装\n"
            f"📅 日付: {datetime.now().strftime('%Y年%m月%d日')}\n\n"
            f"✅ 実施済みタスク\n{tasks_text}\n\n"
            f"📝 習得スキル: ファイル追記(mode='a'), with open\n"
            f"{'-' * 30}\n"
        )

        # 4. 画面に反映
        log_output.value = log_content
        
        # 5. ファイルへ保存
        with open("study_log.txt", mode="a", encoding="utf-8") as f:
            f.write(log_content + "\n")
        
        page.update()

    # レイアウトの構築
    page.add(
        ft.Text("学習ログ作成 (day19 保存機能付き)", size=20, weight=ft.FontWeight.BOLD),
        task_input,
        ft.ElevatedButton("ログ生成", on_click=generate_log),
        log_output
    )

if __name__ == "__main__":
    ft.app(target=main)