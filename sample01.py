# sys: インタプリタや実行環境に関する情報を扱うライブラリ
import sys

# 起動オプションを表示
print(sys.argv, '\n')

# モジュール検索パスの取得
print(sys.path, '\n')

# プラットフォームの取得
print(sys.platform, '\n')

sys.exit()