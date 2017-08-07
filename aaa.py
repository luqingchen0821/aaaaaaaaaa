import pandas as pd

from WindPy import *
w.start()
stock=w.wsi("510050.SH", "close", "2017-01-02 09:00:00", "2017-08-07 13:29:37", "PriceAdj=F")
print(stock.Times[1])

