# tempfile : 一時的なファイルやディレクトリを作成するライブラリ
import tempfile
import os

# 一時ファイルの作成
with tempfile.TemporaryDirectory() as temp_path:
    print(temp_path)
    with open(os.path.join(temp_path, "hoge.txt"), "w"):
        # 一時ファイルが存在するか確認
        print(os.path.exists(os.path.join(temp_path, "hoge.txt")))

# 一時ファイルが削除されている事を確認
print(temp_path)
print(os.path.exists(os.path.join(temp_path, "hoge.txt")))