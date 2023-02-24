import flet as ft
from views.FletRouter import Router
from user_controls.navbar import NavBar

def main(page: ft.Page):
    page.title = "BTCTracker"
    page.theme_mode = "DARK"
    page.window_width = 420
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.appbar = NavBar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

    page.go('/')


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER, port=3333)
#ft.app(target=main, assets_dir="assets")