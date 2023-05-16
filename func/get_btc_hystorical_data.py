from Historic_Crypto import HistoricalData
import datetime
import pandas

def store_data():
    now = datetime.datetime.now()
    start = now - datetime.timedelta(days=90)
    start_string = start.strftime("%Y-%m-%d-%H-%M")
    data = HistoricalData('BTC-EUR',86400,start_string).retrieve_data()
    #remove high,low,open,volume from df
    del data['high']
    del data['low']
    del data['open']
    del data['volume']
    df = pandas.DataFrame(data)
    df.to_csv('data/btc_eur.csv', index=True)


def check_data():
    #read the last line of the csv file
    # if the date is not today, then call store_data()
    # else do nothing
    df = pandas.read_csv('data/btc_eur.csv')
    last_date = df.iloc[-1]['time']
    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d")
    if last_date != now_string:
        store_data()
    else:
        pass

def get_data():
    check_data()
    df = pandas.read_csv('data/btc_eur.csv')
    return df


