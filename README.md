# coinhako-py
Quick and dirty way to get Coinhako BTC/ETH prices (WIP)

## Usage
```python
from coinhako import Coinhako

exchange = Coinhako()
print(exchange.price.BTCSGD())

>> {'status': 'success', 'data': {'buy_price': '2993.14257', 'sell_price': '2953.57347'}}
```

### Endpoints

Coinhako.price

```python
Coinhako.price.BTCUSD()
Coinhako.price.BTCSGD()
Coinhako.price.BTCMYR()
Coinhako.price.ETHUSD()
Coinhako.price.ETHSGD()
Coinhako.price.ETHMYR()
```

See `api_map.py` for more information.