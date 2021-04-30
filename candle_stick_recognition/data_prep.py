import pandas
import requests
import pandas as pd

# link for Bitcoin Data
from candle_stick_recognition.EvaluatorMachine import EvaluatorMachine
from candle_stick_recognition.identify_candlestick import recognize_candlestick
from candle_stick_recognition.take_best_strategy import take_best_strategy

link = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BNB&tsym=USD&limit=100&aggregate=1"

# API request historical
historical_get = requests.get(link)

# access the content of historical api request
historical_json = historical_get.json()

# # extract json data as dictionary
historical_dict = historical_json['Data']['Data']

# # extract Final historical df
df = pd.DataFrame(
    data=historical_dict,
    columns=['close', 'high', 'low', 'open', 'time'],
    dtype='float64'
)

# # time column is converted to "YYYY-mm-dd hh:mm:ss" ("%Y-%m-%d %H:%M:%S")
posix_time = pd.to_datetime(df['time'], unit='s')

# # append posix_time
df.insert(0, "Date", posix_time)

# # drop unix time stamp
df.drop("time", axis=1, inplace=True)

EvaluatorMachine(df, take_best_strategy).evaluate()
