import sys
# os：OSに依存した機能を扱うためのライブラリ
import os

# カレントディレクトリを取得(present working directory)
print(os.getcwd())

# パス区切り文字
print(os.sep)

# パスを親ディレクトリとファイル名に分割
print(os.path.split(sys.argv[0]), '\n')

# パスを連結
print(os.path.join(os.getcwd(), 'hoge.py'), '\n')

# ファイル名を名前と拡張子に分割
print(os.path.splitext('hoge.py'), '/n')
