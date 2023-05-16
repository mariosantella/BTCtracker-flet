import flet as ft

def NavBar(page):
    navbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CURRENCY_BITCOIN),
        leading_width=40,
        title=ft.Text("BTCTracker"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                icon=ft.icons.HOME,
                on_click=lambda e: page.go('/'),
            ),
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                on_click=lambda e: page.go("/settings/"),
            ),
        ],
    )

    return navbar