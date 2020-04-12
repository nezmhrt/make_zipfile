# ①アプリにd&d
# ②選択画面
# ③ファイルをzipで圧縮


import shutil
import sys

url = sys.argv[1]
zip = 'zip'
shutil.make_archive(url, zip, root_dir=url)
