import flet as ft
from flet_route import Routing,path
from user_controls.navbar import NavBar
from views.index_view import IndexView
from views.settings_view import SettingsView

def main(page: ft.Page):
    page.title = "BTCTracker"
    page.theme_mode = "DARK"
    page.window_width = 420
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    app_routes = [
        path(
            url="/", # Here you have to give that url which will call your view on mach
            clear=True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=IndexView # Here you have to pass a function or method which will take page and params and return ft.View (If you are using function based view then you just have to give the name of the function.)
            ), 
        path(url="/settings/", clear=False, view=SettingsView),
    ]

    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        )
    page.go(page.route)
    page.update()


ft.app(target=main, assets_dir="assets",view=ft.WEB_BROWSER, port=3333)
#ft.app(target=main, assets_dir="assets")