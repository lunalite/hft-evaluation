from pandas import DataFrame


class EvaluatorMachine:

    def __init__(self, data: DataFrame, strategy):
        self.data = data
        self.strategy = strategy
        self.cash = 100000
        self.shares = 0

    def evaluate(self):
        buy_list = self.strategy(self.data)

        for idx, row in self.data.iterrows():
            buy = buy_list[idx]
            close_price = float(row['close'])

            if buy == 1 and self.cash > 0:
                self.shares = self.cash / close_price
                self.cash = self.cash - self.shares * close_price
            elif buy == 1 and self.cash == 0:
                continue
            elif buy == 0:
                self.cash = self.cash + self.shares * close_price
                self.shares -= self.shares
            print('close:', close_price, ' shares: ', self.shares, ' cash:', self.cash)
        print('final statement')
        print('close:', close_price)
        print('shares:', self.shares)
        print('cash:', self.cash)
        print('total value:', self.cash + self.shares * close_price)
