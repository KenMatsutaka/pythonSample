# pprint:データ構造を見やすい形に表示(pretty printer)
from pprint import pprint

data = [(i, {'hoge':'HOGE', 'moge':'MOGE'}) for i in range(3)]

print(data)
pprint(data)
