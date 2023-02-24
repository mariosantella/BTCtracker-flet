import flet as ft


def SettingsView(page):

    #TODO - rework wallets balance with new APIs
    """
    def save_wallets(self):
        wallets = wallets_input.value
        page.client_storage.set("wallets", wallets)
        print("Wallets saved!")
    
    #wallets_input = ft.TextField(label="Wallets", hint_text="Enter your wallets here, comma separated", width=400, value=page.client_storage.get("wallets"))
    #save_button = ft.TextButton(text="Save", on_click=save_wallets)
    """

    def save_balance(self):
        balance = balance_input.value
        page.client_storage.set("balance", balance)
        print("Balance saved!")

    balance_input = ft.TextField(label="Balance", hint_text="Enter your BTC balance here", width=400, value=page.client_storage.get("balance"))
    save_button = ft.TextButton(text="Save", on_click=save_balance)

    content = ft.Column(
        [
             ft.Row(
                [
                    ft.Text("Settings", size=25),
                ],
            ),
               ft.Row(
                [
                    ft.Text("Balance", size=18),
                    ft.Text(" - will be stored in ClientStorage", size=16),
                ],
            ),
                ft.Row(
                [
                    balance_input
                ],
            ),
            ft.Row(
                [
                    save_button
                ],
            ),
        ]
    )


    return content
