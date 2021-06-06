from enum import Enum, auto

import talib
from pandas import DataFrame


class Trend(Enum):
    UP = auto()
    DOWN = auto()
    UNKNOWN = auto()


class TrendService:
    def __init__(self, data: DataFrame):
        self.list_of_trends = {}

        sma20 = talib.SMA(data['close'], timeperiod=20)
        sma50 = talib.SMA(data['close'], timeperiod=50)
        date = data['Date']

        for idx, i in enumerate(sma20):
            current_date = '{}-{:02}-{:02}'.format(date[idx].year, date[idx].month, date[idx].day)
            if sma20[idx] == 'nan' or sma50[idx] == 'nan':
                self.list_of_trends[current_date] = Trend.UNKNOWN
            elif sma20[idx] > sma50[idx]:
                self.list_of_trends[current_date] = Trend.UP
            else:
                self.list_of_trends[current_date] = Trend.DOWN

    def get_trend_at_date(self, date: str):
        return self.list_of_trends[date]
