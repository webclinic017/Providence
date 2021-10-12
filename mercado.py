from alpaca_trade_api.rest import REST,TimeFrame
import pandas as pd


class Mercado:

    def __init__(self, agent_hodings: dict, agent_cash: dict, api_key: str, secret_key: str, live: bool) -> None:
        """
        A class used to represent an Animal

        ...

        Attributes
        ----------
        api_key : str
            
        secret_key : str
            
        agent_holdings : dict
            
        agent_cash : dict

        live : bool 
            Define is the bot is going to trade on real time or simulation(ACTIVATE IT WHEN BACKTESTING).
        """
        
        self.api_key = api_key
        self.secret_key = secret_key
        self.agent_holdings = agent_hodings
        self.agent_cash =  agent_cash
        self.live = live

        self.api_account = REST('AKCLP03YEDI2RURGO9WF', '2N7SbDGOgzknPKs1f5QanvQkp7R6qySjenzC7o8a')


    def fetch_stock_data(self, init_date: str, end_date: str, tickers: list, period = 1.0) -> pd.DataFrame:
        
        """
        Fetches data from ALPACA MARKETS
        
        NOTE : period is meaused in seconds,so:
                1 Minute = 60 Seconds 
                1 Day = 3600 Seconds
                1 Month = 216,000 Seconds
                1 Year = 12,960,000 Seconds

        Parameters
        ----------
            init_date: str
                Initial Date of fetching data.
            end_date: str 
                Final Date of fectching data.
            tickers: list
                List of tickers names.
            period: float
                Time-lapse of fetch.
        Returns
        -------
        `pd.DataFrame`
            7 columns: A date, open, high, low, close, volume and tick symbol
            for the specified stock ticker
        """
        # Download and save the data in a pandas DataFrame:
        data_df = pd.DataFrame()
        for tic in self.ticker_list:
            temp_df = self.api.get_bars(tic, TimeFrame.Day, self.start_date , self.end_date, adjustment='raw').df
            temp_df["tic"] = tic
            data_df = data_df.append(temp_df)
        # reset the index, we want to use numbers as index instead of dates
        data_df = data_df.reset_index()
        try:
            # convert the column names to standardized names
            data_df.columns = [
                "date",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "trade_count",
                "vwap",
                'tic'
            ]
            # use adjusted close price instead of close price
            #data_df["close"] = data_df["adjcp"]
            # drop the adjusted close price column
            data_df = data_df.drop("trade_count", 1)
            data_df = data_df.drop("vwap", 1)

        except NotImplementedError:
            print("the features are not supported currently")
        # create day of the week column (monday = 0)
        data_df["day"] = data_df["date"].dt.dayofweek
        # convert date to standard string format, easy to filter
        data_df["date"] = data_df.date.apply(lambda x: x.strftime("%Y-%m-%d"))
        # drop missing data
        data_df = data_df.dropna()
        data_df = data_df.reset_index(drop=True)
        print("Shape of DataFrame: ", data_df.shape)
        # print("Display DataFrame: ", data_df.head())

        data_df = data_df.sort_values(by=['date','tic']).reset_index(drop=True)

        return data_df

    def trade(self, tickers: dict) -> None:
        pass

    def fetch_real_time(self, tickers: list) -> None:
        pass

    def _check_status(self) -> None:
        pass

    def stop(self) -> None:
        pass

