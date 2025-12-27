import flet as ft

def main(page: ft.Page):
    page.title = "営業マンの挨拶ツール"
    page.theme_mode = ft.ThemeMode.LIGHT # 明るいモードに変更
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_input = ft.TextField(
        label="お名前を入力してください", 
        width=300,
        hint_text="例：田中 太郎",
        # Enterキーを押した時に実行
        on_submit=lambda _: on_greet_click(None) 
    )
    
    hello_text = ft.Text(value="", size=25, weight="bold", color="blue")

    def on_greet_click(e):
        if not name_input.value:
            name_input.error_text = "名前を入力してください"
            page.update()
        else:
            hello_text.value = f"✨ こんにちは、{name_input.value}様！ ✨"
            name_input.error_text = None
            page.update()

    page.add(
        ft.Icon(ft.Icons.PERSON_PIN, color="blue", size=50), # アイコン追加
        name_input,
        ft.ElevatedButton(
            "挨拶する", 
            icon=ft.Icons.SEND, # 送信アイコン追加
            on_click=on_greet_click, 
            bgcolor="red", 
            color="white"
        ),
        hello_text
    )

ft.app(target=main)