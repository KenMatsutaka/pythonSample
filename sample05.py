# shelve : キー=値の形でファイルに保存してデータを永続化出来る
# shelveは棚の意味らしい
import shelve

with shelve.open('mydb') as db: 
    # データ の 保存 
    db['key1'] = 'aaa' 
    db['key2'] = 'bbb' 
    db['key3'] = 'ccc' 
    # データ の 読み込み 
    print(db['key1'], db['key2'], db['key3'])
