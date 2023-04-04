import flet as ft
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from classes.get_btc_hystorical_data import hysto
from classes.get_btc_current_price import get_price


price = get_price()

# Plotly chart
figtrend = px.line(hysto, x="time", y="close", title='BTC Price in EUR - Latest 90 days')
figtrend.update_layout(
    plot_bgcolor='rgb(30,30,30)',
    paper_bgcolor='rgb(30,30,30)',
    font_color="white",
    xaxis_title="Date",
    yaxis_title="€",
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


price_container = ft.Container(
        content=ft.Text(str(get_price()) + "€", size=40)
    )

def refresh(self):
    amount = get_price()
    price_container.content.value = str(amount)+"€"
    price_container.content.update()


def TrendView(page):
   
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Current BTC Price:", size=15),
                ],
            ),

            ft.Row(
                [
                    price_container,
                ]
            ),

            ft.Row(
                [
                    PlotlyChart(figtrend, expand=True),
                ]
            ),
            
            ft.Row(
                [
                    ft.FilledButton("Refresh", icon="refresh", on_click=refresh),
                ]
            ),

        ]

    )

    return content
