# logging : ログ出力を扱う為のライブラリ
import logging

# ログの設定
logging.basicConfig(filename="sample13Log.log", level=logging.WARN)
logging.fatal("fatal")
logging.error("error")
logging.warning("warn")
logging.info("into")
logging.debug("debug")