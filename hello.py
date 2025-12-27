import flet as ft

def main(page: ft.Page):
    page.title = "学習ログ生成ツール"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # 入力フィールド
    task_input = ft.TextField(label="実施したタスクを入力", width=400)
    log_display = ft.TextField(
        label="生成されたログ", 
        multiline=True, 
        min_lines=5, 
        read_only=True
    )

    def on_generate_click(e):
        if task_input.value:
            # 既存のログ形式に整形
            formatted_log = f"✅ 実施済みタスク\n[x] {task_input.value}"
            log_display.value = formatted_log
            page.update()

    page.add(
        ft.Text("学習ログ作成アシスタント", size=20, weight="bold"),
        task_input,
        ft.ElevatedButton("ログを生成", on_click=on_generate_click),
        log_display
    )

ft.app(target=main)
