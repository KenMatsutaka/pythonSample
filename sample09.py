# csv : csvファイルを扱うライブラリ
import csv
import sys
try:
    # CSVファイル書き込み
    # ファイルを開く
    with open('sample09.csv', 'w', encoding='utf8') as csvfile:
        #writerオブジェクトの生成
        writer = csv.writer(csvfile, lineterminator='\n')
        #内容の書き込み
        writer.writerow(["a","b","c"])
        writer.writerow(['あ','い','う'])

    # ファイルの読み込み
    # ファイルを開く
    with open('sample09.csv', 'r', encoding='utf8') as csvfile:
        # readerオブジェクトの生成
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError as e:
    print(e)
    sys.exit()
except csv.Error as e:
    print(e)
    sys.exit()

