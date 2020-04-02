
"""

traderalert.py buy EUR/USD
"""

from dataclasses import dataclass, field
from typing import List
import re, sys

@dataclass
class Trade:

    trade_text: str
    stop_loss: float = 0
    entry: float = 0
    profit_level: List[float] = field(default_factory=list)
    symbol: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.parse()

    def parse(self):
        """Extract relevant fields from trade text.

Sample of trade text:

1 month ago
GBP
CAD
TAKE PROFIT
1.72450
Stop loss (SL) - 55 pips
1.71900
Entry price (EP)
I
1.71650
II
1.71300
III
1.70640
3% loss
-55 pips
Id


        :return:
        """
        for line in self.trade_text:
            print(f"TEsting {line}")
            if self.is_forex_symbol(line):
                self.symbol.append(line)
            if self.is_price(line):




    def is_forex_symbol(self, text):
        text = text.rstrip()
        if text == 'III':
            return False
        forex_symbol_re = re.compile('^[A-Z]{3}$')
        m = forex_symbol_re.match(text)
        return m

    def is_price(self, text):
        text = text.rstrip()
        regex = re.compile('[+-]?[0-9]+\.[0-9]+')
        m = regex.match(text)
        return m

    @property
    def is_a_buy(self):
        return self.stop_loss < self.entry

    @property
    def is_a_sell(self):
        return not self.is_a_buy

    @property
    def direction(self):
        if self.is_a_buy:
            return "BUY"
        else:
            return "SELL"


    def __repr__(self):
        return f"symbol: {self.symbol}"

    def __str__(self):
        return """
        Tradera's Trade Team is placing a BUY trade on EUR/GBP at current market price with the following parameters:

Stop Loss 🚫: 0.87902

Take Profit #1 ✅: 0.88383

Take Profit #2 ✅: 0.88865

Take Profit #3 ✅: 0.89836

Additional Notes: Please use proper risk management. 💯

Tradera 🔱
        """

def get_multiline_input():
    print("Paste in the trade text: ")
    lines = sys.stdin.readlines()
    return lines

if __name__ == '__main__':
    trade_text = get_multiline_input()
    trade =Trade(trade_text)
    print(repr(trade))



