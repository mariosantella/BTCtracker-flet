import flet as ft
from func.get_btc_hystorical_data import get_data
from func.get_btc_current_price import get_price
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from flet_route import Params,Basket
from user_controls.navbar import NavBar
import pandas as pd
def IndexView(page:ft.Page,params:Params,basket:Basket):

    price = get_price()
    hysto = get_data()
    
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
    hysto['time'] = pd.to_datetime(hysto['time'])
    #hysto = hysto.set_index('time')
    fig = px.line(hysto, x="time", y="balance", title='BTC Price in EUR')
    fig.update_layout(
        plot_bgcolor='rgb(30,30,30)',
        paper_bgcolor='rgb(30,30,30)',
        font=dict(
        family="Arial",
        color="white"
        ),
        xaxis_title="Date",
        yaxis_title="EUR",
        title_font_size=20,
        title_font_color="white",
        legend_title_font_color="white",
        legend_font_color="white",
        xaxis_title_font_color="white",
        yaxis_title_font_color="white",
        xaxis_tickfont_color="white",
        yaxis_tickfont_color="white",
        xaxis_tickfont=dict(
            family="Arial",
            color="white",
            size=18
        ),
        yaxis_tickfont=dict(
            family="Arial",
            color="white",
            size=18
        ),
        yaxis_tickangle=-45,
        xaxis_tickangle=-45,
        xaxis_tickformat='%d %b',
    )


    chart = PlotlyChart(fig, expand=True)


    current_price_container = ft.Container(
        content=ft.Text("EUR/BTC: " + str(price) + "€", size=20)
    )
    
    def refresh(self):
        balances_sum = float(page.client_storage.get("balance"))
        hysto.drop(columns=["balance"], inplace=True)
        hysto["balance"] = hysto["close"] * balances_sum
        btc_amount = balances_sum
        eur_amount = get_price() * btc_amount
        eur_amount = str(round(eur_amount, 2))
        satoshi_amount = btc_amount * 100000000
        satoshi_amount = int(satoshi_amount)
        balance_container.content.value = str(eur_amount)+"€"
        balance_container.content.update()
        price = get_price()
        current_price_container.content.value = "EUR/BTC: " + str(price) + "€"
        current_price_container.update()    

        # TODO: make the graph update

    return ft.View( 
        "/",
        controls=[
            NavBar(page),
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
                    chart
                ],
            ),

            ft.Row(
                [
                    ft.FilledButton("Refresh", icon="refresh", on_click=refresh),
                    current_price_container
                ]
            ),
        ],
    )