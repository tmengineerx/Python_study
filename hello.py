import flet as ft
from datetime import datetime # 日付を扱うための道具をインポート

def main(page: ft.Page):
    page.title = "学習ログ生成ツール"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 入力フィールド
    task_input = ft.TextField(label="実施したタスクを入力", width=400)
    log_display = ft.TextField(
        label="生成されたログ", 
        multiline=True, 
        min_lines=8, 
        read_only=True
    )

    def on_generate_click(e):
        if task_input.value:
            # ボタンを押した瞬間の日付を取得
            today_str = datetime.now().strftime("%Y年%m月%d日")
            
            # テンプレートの形式に整形
            formatted_log = (
                f"📅 日付\n"
                f"{today_str}\n\n"
                f"✅ 実施済みタスク\n"
                f"[x] {task_input.value}"
            )
            
            log_display.value = formatted_log
            page.update()

    page.add(
        ft.Icon(ft.Icons.EDIT_NOTE, color="blue", size=50),
        ft.Text("学習ログ作成アシスタント", size=20, weight="bold"),
        task_input,
        ft.ElevatedButton("ログを生成", on_click=on_generate_click, bgcolor="red", color="white"),
        log_display
    )

ft.app(target=main)