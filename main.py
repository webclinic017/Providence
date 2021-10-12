from alpaca_trade_api.rest import REST,TimeFrame
import pandas as pd

if __name__ == '__main__':
    


    api = REST('AKCLP03YEDI2RURGO9WF', '2N7SbDGOgzknPKs1f5QanvQkp7R6qySjenzC7o8a')

    bars = api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df

    print(bars.head())