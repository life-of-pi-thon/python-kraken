#!/usr/bin/env python3

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# To debug historic OHLC data inconcistencies, as discussed here:
# https://www.reddit.com/r/kraken_traders/comments/6f6e9h/krakenapi_delivering_inconsistent_false_ohlc_data/

import krakenex

import decimal
import time
k = krakenex.API()

all_pairs = k.query_public('AssetPairs')
all_pairs_keys = ','.join(all_pairs['result'].keys())
print(all_pairs_keys)

ret = k.query_public('Ticker', data={'pair': all_pairs_keys})
print(ret)

