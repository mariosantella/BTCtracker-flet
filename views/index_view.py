import flet as ft
from classes.get_btc_hystorical_data import hysto
from classes.get_btc_current_price import price
import plotly.express as px
from flet.plotly_chart import PlotlyChart


def IndexView(page):

    # get the balance from the client storage without crashing if is null

    if page.client_storage.get("balance") == None:
        balances_sum = 1
        page.client_storage.set("balance", 1)
    else:
        balances_sum = float(page.client_storage.get("balance"))
    hysto["balance"] = hysto["close"] * balances_sum
    btc_amount = balances_sum
    eur_amount = price * btc_amount
    eur_amount = str(round(eur_amount, 2))
    satoshi_amount = btc_amount * 100000000
    satoshi_amount = int(satoshi_amount)

    def change_balance(self):
        # this function will switch the balance from BTC to EUR and to SAT and back
        # and update the balance_container

        if balance_container.content.value == str(btc_amount)+"₿":
            balance_container.content = ft.Text(str(eur_amount)+"€", size=40)
            balance_container.update()
        elif balance_container.content.value == str(eur_amount)+"€":
            balance_container.content = ft.Text(
                str(satoshi_amount)+" SAT", size=40)
            balance_container.update()
        elif balance_container.content.value == str(satoshi_amount)+" SAT":
            balance_container.content = ft.Text(str(btc_amount)+"₿", size=40)
            balance_container.update()
        else:
            balance_container.content = ft.Text(str(btc_amount)+"₿", size=40)
            balance_container.update()

    balance_container = ft.Container(
        content=ft.Text(str(eur_amount)+"€", size=40),
        on_click=change_balance
    )

    # using hysto to make a dark theme plotly chart
    fig = px.line(hysto, x="time", y="balance", title='BTC Price in EUR')
    fig.update_layout(
        plot_bgcolor='rgb(30,30,30)',
        paper_bgcolor='rgb(30,30,30)',
        font_color="white",
        xaxis_title="Date",
        yaxis_title="Price in EUR",
        title_font_size=20,
        title_font_color="white",
        legend_title_font_color="white",
        legend_font_color="white",
        xaxis_title_font_color="white",
        yaxis_title_font_color="white",
        xaxis_tickfont_color="white",
        yaxis_tickfont_color="white",
        xaxis_tickformat='%d %b',
    )

    balance_graph = PlotlyChart(fig, expand=True)

    def refresh(self):
        balances_sum = float(page.client_storage.get("balance"))
        hysto.drop(columns=["balance"], inplace=True)
        hysto["balance"] = hysto["close"] * balances_sum
        btc_amount = balances_sum
        eur_amount = price * btc_amount
        eur_amount = str(round(eur_amount, 2))
        satoshi_amount = btc_amount * 100000000
        satoshi_amount = int(satoshi_amount)
        balance_container.content.value = str(eur_amount)+"€"
        balance_container.content.update()

        # TODO: make the graph update
      

    content = ft.Column(
        [

            ft.Row(
                [
                    ft.Text("Balance:", size=15),
                ],
            ),
            ft.Row(
                [
                    balance_container
                ]
            ),
            ft.Row(
                [
                    balance_graph
                ],
            ),

            ft.Row(
                [
                    ft.FilledButton("Refresh", icon="refresh", on_click=refresh),
                ]
            ),
        ],
    )

    return content
